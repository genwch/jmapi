from . import auth
from . import jobcat
from . import data
import models as mod

debug = False

__routes__ = [auth.router, jobcat.router]

for k, v in mod.__model__.items():
    __routes__.append(data.data_rt(mod_name=k, debug=debug).router)
