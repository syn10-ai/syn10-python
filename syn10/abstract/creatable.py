import syn10
from syn10 import utils
from syn10.api_requestor import APIRequestor


class Creatable:
    @staticmethod
    def get_endpoint():
        raise NotImplementedError

    @classmethod
    def _construct_obj_from_id(cls, id):
        raise NotImplementedError

    @classmethod
    def create(cls, *args, **params):
        requestor = APIRequestor(token=utils.find_token())
        url = f"{syn10.base}{cls.get_endpoint()}"
        resp = requestor._request("POST", url, data=params, query={"cls": cls.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        obj = cls._construct_obj_from_id(resp_json.get("id"))
        return obj

