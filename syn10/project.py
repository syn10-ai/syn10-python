__all__ = [
    "Project"
]

import syn10
from syn10 import TrainingOrder, SamplingOrder
from syn10.abstract import (
    Informable,
    Creatable,
    Updatable,
    Listable,
    Deletable
)

from typing import Type, Union


class Project(Informable, Creatable, Updatable, Listable, Deletable):
    def __init__(self, id):
        super().__init__(id=id)
        self.id = id

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

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

    def create_order(
            self,
            type: Union[Type[SamplingOrder], Type[TrainingOrder]],
            **parameters
    ):
        order = type.create(project_id=self.get_id(), **parameters)
        return order

    def get_orders(
            self,
            type: Union[Type[SamplingOrder], Type[TrainingOrder]]
    ):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/orders"
        resp = self.request("GET", url, query={"cls": type.__name__})
        resp.raise_for_status()
        resp_json = resp.json()
        return [type(id=order.get("id")) for order in resp_json]



