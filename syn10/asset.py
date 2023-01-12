__all__ = [
    "Dataset",
    "Deliverable"
]

from syn10.abstract import (
    APIResource,
    Listable,
    Creatable,
    Downloadable,
    Deletable,
    Informable,
    Updatable
)


class Asset(APIResource):
    def __init__(self, id):
        super().__init__(id=id)
        self.id = id

    @staticmethod
    def get_endpoint():
        return "/assets"


class Dataset(Asset, Informable, Listable, Creatable, Updatable, Deletable, Downloadable):
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


class Deliverable(Asset, Informable, Listable, Downloadable, Deletable):
    def __init__(self, id):
        super(Deliverable, self).__init__(id=id)

    def download(self):
        resp = super().download(id=self.id)
        return resp

