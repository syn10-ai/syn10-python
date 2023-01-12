__all__ = [
    "Model"
]

import syn10
from syn10.abstract import (
    Informable,
    Listable,
    Deletable
)


class Model(Informable, Listable, Deletable):
    def __init__(self, id):
        super().__init__(id=id)
        self.id = id

    @staticmethod
    def get_endpoint():
        return "/models"

    @property
    def policy(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/policy"
        resp = self.request("GET", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json

    @property
    def verified(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/verified"
        resp = self.request("GET", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json.get("verified")

    def verify(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/verify"
        resp = self.request("POST", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json

