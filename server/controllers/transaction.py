from os import getenv
from datetime import datetime
import requests
from rave_python.rave_misc import generateTransactionReference
from rave_python import Rave
from flask import request, jsonify, abort
from ..controllers.user import user_controller
from ..models.transaction import Transaction
from ..utils.response import generate_response
from .. import db

rave = Rave(getenv("FLW_PUBLIC_KEY"), getenv("FLW_SECRET_KEY"), usingEnv=False)


class TransactionController:
    FRONTEND_REDIRECT_URL = "/payment/confirm"
    FLW_CREATE_PAYMENT_URL = "https://api.flutterwave.com/v3/payments"

    def create_payment_link(self, amount, currency, txn_ref):
        headers = {
            "Authorization": f"Bearer {getenv('FLW_SECRET_KEY')}",
            "Content-Type": "application/json",
        }
        payload = {
            "tx_ref": txn_ref,
            "amount": amount,
            "currency": currency,
            "redirect_url": self.FRONTEND_REDIRECT_URL,
            "meta": {
                "consumer_id": request.current_user.id,
            },
            "customer": {
                "email": request.current_user.email,
                "name": f"{request.current_user.fname} {request.current_user.lname}",
            },
            "customizations": {
                "title": "Border Link",
                "logo": "",
            },
        }

        try:
            response = requests.post(
                self.FLW_CREATE_PAYMENT_URL, headers=headers, json=payload
            )
            response.raise_for_status()  # Raise an error for HTTP error responses
            result = response.json()
            return result
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            raise
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            raise
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            raise
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")
            raise

    def fund_wallet(self):
        # extract json
        amount = request.json.get("amount")
        currency = request.json.get("currency")

        if amount is None or currency is None:
            abort(400)

        txn = Transaction()
        txn.txn_type = "credit"
        txn.description = "fund wallet"
        txn.action = "fund wallet"
        txn.txn_status = "pending"
        txn.amount = amount
        txn.txn_ref = generateTransactionReference()
        txn.currency_from = currency
        txn.currency_to = currency
        txn.from_user = request.current_user.id

        db.session.add(txn)
        db.session.commit()

        return self.create_payment_link(amount, currency, txn.txn_ref)

    def webhook(self):
        print("webhook called")
        secret_hash = getenv("FLW_SECRET_HASH")
        signature = request.headers.get("verifi-hash")

        if signature is None or (signature != secret_hash):
            # This request isn't from Flutterwave; discard
            return jsonify({"message": "Unauthorized"}), 401

        payload = request.get_json().get("data")
        txn_ref = payload.get("tx_ref")

        txn = Transaction.query.filter_by(txn_ref=txn_ref).first()
        if txn is None:
            return abort(404)

        confirmation = rave.Account.verify(txn_ref)
        if confirmation.get("status") == "success":
            if txn.credited == "N":
                txn.status = payload.get("status")
                txn.txn_time = datetime.strptime(
                    payload.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ"
                )

                if txn.description == "fund wallet":
                    self.credit_user(
                        request.current_user.id, float(confirmation.get("amount"))
                    )
                txn.credited = "Y"
                db.session.add(txn)
                db.session.commit()
        return jsonify({"message": "Webhook received successfully"}), 200

    def credit_user(self, user_id, amount):
        user = user_controller.get_by_id(user_id)
        user.acc_balance += amount

        db.session.add(user)
        db.session.commit()
        print(user)


transaction_controller = TransactionController()
