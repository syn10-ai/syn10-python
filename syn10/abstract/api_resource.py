from syn10.api_requestor import APIRequestor
from syn10 import utils


class APIResource:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    @staticmethod
    def get_endpoint():
        return NotImplementedError

    @classmethod
    def _construct_obj_from_id(cls, id):
        return cls(id=id)

    @classmethod
    def _construct_list_from_resp(cls, resp):
        return [cls._construct_obj_from_id(item.get("id")) for item in resp]

    @staticmethod
    def request(*args, **kwargs):
        requestor = APIRequestor(token=utils.find_token())
        resp = requestor.request(*args, **kwargs)
        return resp
