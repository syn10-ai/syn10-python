__all__ = [
    "TrainingOrder",
    "SamplingOrder"
]

import syn10
from syn10.api_requestor import APIRequestor
from syn10 import utils


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
        self.info = resp.json()
        self.project_id = ...
        self.order_parameters = ...

    def place(self):
        raise NotImplementedError

    def estimate(self, estimation_parameters={}):
        raise NotImplementedError

    def get_assets(self, json=False):
        pass

    def status(self):
        pass

    def cancel(self):
        pass


class TrainingOrder(Order):
    def __init__(self, order_id=None, project_id=None, order_parameters={}):
        super(TrainingOrder, self).__init__(
            order_id=order_id,
            project_id=project_id,
            order_parameters=order_parameters
        )

    def place(self):
        print(
            f"placing training order ... "
            f"project_id: {self.project_id} "
            f"order_parameters: {self.order_parameters}"
        )

    def get_models(self):
        if not self.order_id:
            return []
        ...


class SamplingOrder(Order):
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

        # TODO: place order

        print(
            f"placing sampling order ... "
            f"project_id: {self.project_id} "
            f"order_parameters: {self.order_parameters}"
        )

    def estimate(self, estimation_parameters={}):
        estimation_parameters.update(self.order_parameters)
        if "_purpose" in estimation_parameters:
            raise KeyError('"_purpose" is a reserved keyword.')
        estimation_parameters.update({"_purpose": "sampling"})

        model_id = estimation_parameters.get("model_id")
        assert model_id
        utils.check_model_verified(model_id=model_id)

        url = f"{syn10.base}{self.get_endpoint()}/estimate"
        resp = self._request("POST", url, data=estimation_parameters)
        resp.raise_for_status()
        return resp.json()


