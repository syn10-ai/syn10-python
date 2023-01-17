import os
import logging

import syn10
from syn10 import main

logger = logging.getLogger("syn10")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def find_token():
    return syn10.token or main._auth.token if main._auth is not None else None


def check_model_verified(model_id):
    model = syn10.Model(id=model_id)
    if model.verified is False:
        raise Exception(f"model_id: {id} is not verified.")


def _log_level():
    if syn10.debug:
        return "debug"
    elif syn10.log:
        return syn10.log
    elif os.getenv("SYN10_LOG"):
        return os.getenv("SYN10_LOG")
    else:
        return "info"


def _fmt(message, kwargs):
    params = [message]
    for k, v in kwargs.items():
        params.append("%s=%r" % (k, v))
    msg = ", ".join(params)
    return msg


def log_debug(message: str, /, **kwargs):
    msg = _fmt(message, kwargs)
    if _log_level() == "debug":
        logger.debug(msg)


def log_info(message: str, /, **kwargs):
    msg = _fmt(message, kwargs)
    if _log_level() in ["debug", "info"]:
        logger.info(msg)


def log_warning(message: str, /, **kwargs):
    msg = _fmt(message, kwargs)
    if _log_level() in ["debug", "info", "warning"]:
        logger.warning(msg)


def log_error(message: str, /, **kwargs):
    msg = _fmt(message, kwargs)
    if _log_level() in ["debug", "info", "warning", "error"]:
        logger.error(msg)


def log_critical(message: str, /, **kwargs):
    msg = _fmt(message, kwargs)
    if _log_level() in ["debug", "info", "warning", "error", "critical"]:
        logger.critical(msg)
