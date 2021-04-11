import pddb


class profiles_mod(pddb.pdtbl):
    def init_obj(self) -> dict:
        acl = pddb.ACL.SHARED
        path = "./data/profiles.parquet"
        obj = {"pid": {"type": str, "uuid": True, "ignupd": True},
               "usr_cde": {"type": str, "key": True},
               "usr_name": {"type": str},
               "email": {"type": str},
               "usr_desc": {"type": str},
               "education": {"type": str},
               "qualification": {"type": str},
               "work_exp": {"type": str},
               "programing": {"type": str},
               "job_cat": {"type": str},
               "status": {"type": bool, "default": True}}
        return (obj, path, acl)
