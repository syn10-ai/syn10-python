__all__ = [
    "Project"
]

from typing import Type, Union

import syn10
from syn10.order import Order
from syn10.api_requestor import APIRequestor
from syn10.abstract import (
    Informable,
    Creatable,
    Updatable,
    Listable,
    Deletable
)


class Project(APIRequestor, Informable, Creatable, Updatable, Listable, Deletable):
    def __init__(self, id):
        super(Project, self).__init__()
        self.id = id

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

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
        return "/projects"

    @classmethod
    def create(cls, name, metadata={}):
        payload = {
            "name": name,
            "metadata": metadata
        }
        project = super().create(**payload)
        return project

    def create_order(self, order_type: Union[Type[Order], Type[Creatable]], **parameters):
        order = order_type.create(project_id=self.get_id(), **parameters)
        return order

    def get_orders(self, order_type: Type[Order]):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/orders"
        resp = self._request("GET", url, query={"cls": order_type.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return [order_type(id=order.get("id")) for order in resp_json]






