__all__ = [
    "Order",
    "TrainingOrder",
    "SamplingOrder"
]

import syn10
from syn10.api_requestor import APIRequestor
from syn10 import utils
from syn10.abstract import Listable


class Order(APIRequestor):
    def __init__(
            self,
            order_id=None,
            project_id=None,
            order_parameters={}
    ):
        super(Order, self).__init__()
        self.order_id = order_id
        self.project_id = project_id
        self.order_parameters = order_parameters
        self.info = None

        if self.order_id:
            self._fetch_info()

    @staticmethod
    def get_endpoint():
        return "/orders"

    def _fetch_info(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.order_id}/info"
        resp = self._request("GET", url)
        resp.raise_for_status()
        resp_json = resp.json()
        self.info = resp_json
        self.project_id = resp_json.get("project_id")
        self.order_parameters = resp_json.get("order_parameters")

    def place(self):
        raise NotImplementedError

    def estimate(self, estimation_parameters={}):
        raise NotImplementedError

    def get_assets(self):
        if not self.order_id:
            return []
        url = f"{syn10.base}{self.get_endpoint()}/{self.order_id}/assets"
        resp = self._request("GET", url)
        resp.raise_for_status()
        resp_json = resp.json()
        return [syn10.Asset(id=asset.get("id")) for asset in resp_json]

    def status(self):
        pass

    def cancel(self):
        pass


class TrainingOrder(Order, Listable):
    def __init__(self, order_id=None, project_id=None, order_parameters={}):
        super(TrainingOrder, self).__init__(
            order_id=order_id,
            project_id=project_id,
            order_parameters=order_parameters
        )

    def place(self):
        if self.order_id:
            raise Exception(
                "'order_id' should not be provided "
                "for a new order placement"
            )

        url = f"{syn10.base}{self.get_endpoint()}/place"
        payload = self.order_parameters.copy()
        payload.update(
            {
                "order_id": self.order_id,
                "project_id": self.project_id,
                "order_class": self.__class__.__name__
            }
        )
        resp = self._request("POST", url, data=payload)
        resp.raise_for_status()
        return resp

    def get_models(self):
        model_ids = []
        if not self.order_id:
            return model_ids
        url = f"{syn10.base}{self.get_endpoint()}/{self.order_id}/models"
        resp = self._request("GET", url)
        resp.raise_for_status()
        model_ids = resp.json().get("model_ids", [])
        if not model_ids:
            return model_ids
        models = [syn10.Model(model_id=model_id) for model_id in model_ids]
        return models

    def estimate(self, estimation_parameters={}):
        raise NotImplementedError


class SamplingOrder(Order, Listable):
    def __init__(self, order_id=None, project_id=None, order_parameters={}):
        super(SamplingOrder, self).__init__(
            order_id=order_id,
            project_id=project_id,
            order_parameters=order_parameters
        )

    def place(self):
        if self.order_id:
            raise Exception(
                "'order_id' should not be provided "
                "for a new order placement"
            )

        model_id = self.order_parameters.get("model_id")
        assert model_id
        utils.check_model_verified(model_id=model_id)

        url = f"{syn10.base}{self.get_endpoint()}/place"
        payload = self.order_parameters.copy()
        payload.update(
            {
                "order_id": self.order_id,
                "project_id": self.project_id,
                "order_class": self.__class__.__name__
            }
        )
        resp = self._request("POST", url, data=payload)
        resp.raise_for_status()
        return resp

    def estimate(self, estimation_parameters={}):
        estimation_parameters.update(self.order_parameters)
        if "order_class" in estimation_parameters:
            raise KeyError('"order_class" is a reserved keyword.')
        estimation_parameters.update({"order_class": self.__class__.__name__})

        model_id = estimation_parameters.get("model_id")
        assert model_id
        utils.check_model_verified(model_id=model_id)

        url = f"{syn10.base}{self.get_endpoint()}/estimate"
        resp = self._request("POST", url, data=estimation_parameters)
        resp.raise_for_status()
        return resp.json()
