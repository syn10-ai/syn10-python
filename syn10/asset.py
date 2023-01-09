__all__ = [
    "Dataset",
    "Deliverable"
]

from syn10.api_requestor import APIRequestor
from syn10.abstract import (
    Listable,
    Creatable,
    Downloadable,
    Deletable,
    Informable,
    Updatable
)


class Asset(APIRequestor, Informable):
    def __init__(self, id=None):
        super(Asset, self).__init__()
        self.id = id

    def get_id(self):
        if not self.id:
            raise ValueError("'id' is missing.")
        return self.id

    @staticmethod
    def get_endpoint():
        return "/assets"

    @classmethod
    def _construct_obj_from_id(cls, id):
        return cls(id=id)

    @classmethod
    def _construct_list_from_resp(cls, resp):
        return [
            cls._construct_obj_from_id(
                item.get("id")
            ) for item in resp
        ]


class Dataset(
    Asset,
    Creatable,
    Listable,
    Updatable,
    Deletable,
    Downloadable
):
    def __init__(self, id):
        super(Dataset, self).__init__(id=id)

    @classmethod
    def create(cls, path=None, metadata={}):
        payload = {
            "path": path,
            "metadata": metadata
        }
        dataset = super().create(**payload)
        return dataset

    def download(self):
        resp = super().download(id=self.id)
        return resp


class Deliverable(Asset, Downloadable, Listable, Deletable):
    def __init__(self, id):
        super(Deliverable, self).__init__(id=id)

    def download(self):
        resp = super().download(id=self.id)
        return resp

