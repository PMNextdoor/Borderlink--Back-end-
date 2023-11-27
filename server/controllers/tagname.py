from ..controllers.user import user_controller


class TagnameController:
    def verify(self, tagname):
        user = user_controller.get_by_tagname(tagname)
        print(user)
        if user is None:
            return True
        return False


tagname_controller = TagnameController()
