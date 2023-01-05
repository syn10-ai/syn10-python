__all__ = [
    "Project"
]

import syn10
from syn10.order import Order
from syn10.api_requestor import APIRequestor
from syn10 import utils
from syn10.abstract import Listable


class Project(APIRequestor, Listable):
    def __init__(
            self,
            **kwargs
    ):
        super(Project, self).__init__()
        self.project_id = kwargs.get("id")
        self.project_name = kwargs.get("name")

    def __enter__(self):
        if self.project_id:
            self._get_project()
        elif self.project_name:
            self._create_project()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def get_endpoint():
        return "/projects"

    def _create_project(self):
        print(f"creating project with name: {self.project_name}")
        self.project_id = "sdjh98w4"

    def _get_project(self):
        print(f"getting project with id: {self.project_id}")
        self.project_name = "sjkdf"

    def place(self, order: Order = None):
        order.project_id = self.project_id
        order.place()

    def get_orders(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.project_id}/orders"
        resp = self._request("GET", url)
        resp.raise_for_status()
        orders_ = resp.json().get("orders", [])
        orders = [Order(order_id=order.get("order_id")) for order in orders_]
        return orders

    def delete(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.project_id}/delete"
        resp = self._request("DELETE", url)
        resp.raise_for_status()
        return resp





