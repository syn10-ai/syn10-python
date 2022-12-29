__all__ = [
    "Model"
]

import syn10
from syn10.api_requestor import APIRequestor


class Model(APIRequestor):
    def __init__(
            self,
            model_id=None
    ):
        super(Model, self).__init__()
        self.model_id = model_id

    @staticmethod
    def get_endpoint():
        return "/models"

    @property
    def policy(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.model_id}/policy"
        resp = self._request("GET", url)
        resp.raise_for_status()
        return resp.json()

    @property
    def verified(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.model_id}/verified"
        resp = self._request("GET", url)
        resp.raise_for_status()
        return resp.json().get("verified", False)

    @property
    def info(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.model_id}/info"
        resp = self._request("GET", url)
        resp.raise_for_status()
        return resp.json()

    def verify(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.model_id}/verify"
        resp = self._request("POST", url)
        resp.raise_for_status()
        return resp.json()
