__all__ = [
    "Dataset"
]

import json

import syn10
from syn10.api_requestor import APIRequestor


class Asset(APIRequestor):
    def __init__(self, asset_id=None, metadata=None):
        super(Asset, self).__init__()
        self.asset_id = asset_id
        self.info = metadata

        if self.asset_id:
            self._fetch_info()

    @staticmethod
    def get_endpoint():
        return "/assets"

    def _fetch_info(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.asset_id}/info"
        resp = self._request("GET", url)
        resp.raise_for_status()
        self.info = resp.json()

    def update_metadata(self, metadata={}, replace=False):
        if self.asset_id:
            url = f"{syn10.base}{self.get_endpoint()}/{self.asset_id}/metadata"
            resp = self._request("POST", url, data=metadata, query={"replace": replace})
            resp.raise_for_status()
            self._fetch_info()
        else:
            self.info = metadata if replace is True else self.info.update(metadata)


class Downloadable(Asset):
    def _download(self, *args, **kwargs):
        pass


class Uploadable(Asset):
    def _upload(self, *args, **kwargs):
        pass


class Deletable(Asset):
    def _delete(self, *args, **kwargs):
        pass


class Dataset(Uploadable, Downloadable, Deletable):
    def __init__(self, asset_id=None, filepath=None, metadata=None):
        super(Dataset, self).__init__(asset_id=asset_id, metadata=metadata)
        self.filepath = filepath

    def upload(self):
        self._upload(self.filepath, self.info)

    def download(self):
        self._download(self.asset_id)

    def delete(self):
        self._delete(self.asset_id)


