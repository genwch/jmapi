from .users import *
from .profiles import *
from .token import *
from .jobs import *
from .applies import *
from .offers import *
from .comments import *
from .jobcat import *

__model__ = {"users": users_mod, "profiles": profiles_mod, "jobs": jobs_mod,
             "applies": applies_mod, "offers": offers_mod, "comments": comments_mod}
