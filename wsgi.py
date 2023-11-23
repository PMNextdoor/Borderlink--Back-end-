from dotenv import load_dotenv, find_dotenv
from server import app

load_dotenv(find_dotenv())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
