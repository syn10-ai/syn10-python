import syn10
from syn10.api_requestor import APIRequestor
from syn10 import utils


class Listable:
    @staticmethod
    def get_endpoint():
        raise NotImplementedError

    @classmethod
    def _construct_list_from_resp(cls, resp_json):
        raise NotImplementedError

    @classmethod
    def list(cls):
        url = f"{syn10.base}{cls.get_endpoint()}"
        requestor = APIRequestor(token=utils.find_token())
        resp = requestor._request("GET", url, query={"cls": cls.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        list_of_cls_obj = cls._construct_list_from_resp(resp_json)
        return list_of_cls_obj
