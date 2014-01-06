

from pybb.permissions import DefaultPermissionHandler


class PermissionHandler(DefaultPermissionHandler):
    def may_create_poll(self, user):
        """
        return True if `user` may attach files to posts, False otherwise.
        By default always False
        """
        return False
