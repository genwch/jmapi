import pddb


class offers_mod(pddb.pdtbl):
    def init_obj(self) -> dict:
        acl = pddb.ACL.SHARED
        # acl = pddb.ACL.PRIVATE
        path = "./data/offers.parquet"
        obj = {"oid": {"type": str, "uuid": True, "ignupd": True},
               "job_cde": {"type": str, "require": True, "key": True},
               "aid": {"type": str, "require": True},
               "rate": {"type": str},
               "status": {"type": bool, "default": True}}
        return (obj, path, acl)
