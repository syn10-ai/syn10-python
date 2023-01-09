__all__ = [
    "Model"
]

import syn10
from syn10.api_requestor import APIRequestor
from syn10.abstract import (
    Informable,
    Listable,
    Deletable
)


class Model(APIRequestor, Informable, Listable, Deletable):
    def __init__(self, id):
        super(Model, self).__init__()
        self.id = id

    def get_id(self):
        return self.id

    @classmethod
    def _construct_obj_from_id(cls, id):
        return cls(id=id)

    @classmethod
    def _construct_list_from_resp(cls, resp):
        return [cls._construct_obj_from_id(item.get("id")) for item in resp]

    @staticmethod
    def get_endpoint():
        return "/models"

    @property
    def policy(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/policy"
        resp = self._request("GET", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json

    @property
    def verified(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/verified"
        resp = self._request("GET", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json.get("verified")

    def verify(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/verify"
        resp = self._request("POST", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json

