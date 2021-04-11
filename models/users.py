import pddb


class users_mod(pddb.pdtbl):
    def init_obj(self) -> dict:
        acl = pddb.ACL.SHARED
        path = "./data/users.parquet"
        obj = {"uid": {"type": str, "uuid": True, "ignupd": True},
               "usr_cde": {"type": str, "key": True},
               "password": {"type": str, "require": True, "md5": True},
               "status": {"type": bool, "default": True}}
        return (obj, path, acl)
