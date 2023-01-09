__all__ = [
    "TrainingOrder",
    "SamplingOrder"
]

import syn10
from syn10.api_requestor import APIRequestor
from syn10 import utils
from syn10.abstract import (
    Informable,
    Listable,
    Deletable,
    Creatable,
    Cancelable
)


class Order(APIRequestor, Informable):
    def __init__(self, id):
        super(Order, self).__init__()
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
        return "/orders"

    def get_deliverables(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/deliverables"
        resp = self._request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return [syn10.Deliverable(id=deliverable.get("id")) for deliverable in resp_json]

    @classmethod
    def estimate(cls, **parameters):
        url = f"{syn10.base}{cls.get_endpoint()}/estimate"
        requestor = APIRequestor(token=utils.find_token())
        resp = requestor._request("POST", url, data=parameters, query={"cls": cls.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return resp_json

    @property
    def status(self):
        _status = self.info.get("status")
        return _status


class TrainingOrder(Order, Creatable, Listable, Cancelable, Deletable):
    def __init__(self, id):
        super(TrainingOrder, self).__init__(id=id)

    @classmethod
    def create(cls, project_id, **parameters):
        payload = {
            "project_id": project_id,
            "parameters": parameters
        }
        order = super().create(**payload)
        return order

    def get_models(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/models"
        resp = self._request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        models = [syn10.Model(id=model.get("id")) for model in resp_json]
        return models

    @classmethod
    def estimate(cls, **parameters):
        raise NotImplementedError


class SamplingOrder(Order, Creatable, Listable, Cancelable, Deletable):
    def __init__(self, id):
        super(SamplingOrder, self).__init__(id=id)

    @classmethod
    def create(cls, project_id, **parameters):
        model_id = parameters.get("model_id")
        if not model_id:
            raise KeyError("'model_id' is missing.")
        utils.check_model_verified(model_id=model_id)
        payload = {
            "project_id": project_id,
            "parameters": parameters
        }
        order = super().create(**payload)
        return order

    @classmethod
    def estimate(cls, **parameters):
        model_id = parameters.get("model_id")
        if not model_id:
            raise KeyError("'model_id' is missing.")
        utils.check_model_verified(model_id=model_id)
        estimation = super().estimate(**parameters)
        return estimation
