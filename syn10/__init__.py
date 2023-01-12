import os
from syn10.main import *
from syn10.order import *
from syn10.project import *
from syn10.asset import *
from syn10.model import *

token = os.getenv("SYN10_TOKEN")
base = os.getenv("SYN10_BASE", "http://127.0.0.1:8000")

debug = False
log = None

# if debug:
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # dev purpose only
