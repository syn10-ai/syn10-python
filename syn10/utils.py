import syn10
from syn10 import main


def find_token():
    return syn10.token or main._auth.token if main._auth is not None else None


def check_model_verified(model_id=None):
    model = syn10.Model(model_id=model_id)
    if model.verified is False:
        raise Exception(
            f"model_id: {model_id} is not verified."
        )
