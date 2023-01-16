__all__ = [
    "TrainingOrder",
    "SamplingOrder"
]

import syn10
from syn10.api_requestor import APIRequestor
from syn10 import utils
from syn10.abstract import (
    APIResource,
    Informable,
    Listable,
    Deletable,
    Creatable,
    Cancelable
)


class Order(APIResource):
    def __init__(self, id):
        super().__init__(id=id)
        self.id = id

    @staticmethod
    def get_endpoint():
        return "/orders"

    def get_deliverables(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/deliverables"
        resp = self.request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return [syn10.Deliverable(id=deliverable.get("id")) for deliverable in resp_json]

    @classmethod
    def estimate(cls, **params):
        url = f"{syn10.base}{cls.get_endpoint()}/estimate"
        requestor = APIRequestor(token=utils.find_token())
        resp = requestor.request("POST", url, data=params, query={"cls": cls.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json

    @property
    def status(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/status"
        resp = self.request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json


class TrainingOrder(Order, Informable, Creatable, Listable, Cancelable, Deletable):
    def __init__(self, id):
        super(TrainingOrder, self).__init__(id=id)

    @classmethod
    def create(cls, project_id, **params):
        payload = {
            "project_id": project_id,
            "params": params
        }
        order = super().create(**payload)
        return order

    def get_models(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/models"
        resp = self.request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        models = [syn10.Model(id=model.get("id")) for model in resp_json]
        return models

    @classmethod
    def estimate(cls, **params):
        raise NotImplementedError


class SamplingOrder(Order, Informable, Creatable, Listable, Cancelable, Deletable):
    def __init__(self, id):
        super(SamplingOrder, self).__init__(id=id)

    @classmethod
    def create(cls, project_id, **params):
        model_id = params.get("model_id")
        if not model_id:
            raise KeyError("'model_id' is missing.")
        utils.check_model_verified(model_id=model_id)
        payload = {
            "project_id": project_id,
            "params": params
        }
        order = super().create(**payload)
        return order

    @classmethod
    def estimate(cls, **params):
        model_id = params.get("model_id")
        if not model_id:
            raise KeyError("'model_id' is missing.")
        estimation = super().estimate(**params)
        return estimation
