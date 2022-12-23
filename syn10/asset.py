__all__ = [
    "Dataset"
]


class Asset:
    def __init__(self, asset_id=None, asset_info=None):
        self.asset_id = asset_id
        self._info = asset_info

        if self.asset_id:
            self._info = self.info

    @property
    def info(self):
        return {"tags": ["tag-1", "tag-2"]}


class Downloadable(Asset):
    def _download(self, *args, **kwargs):
        pass


class Uploadable(Asset):
    def _upload(self, *args, **kwargs):
        pass


class Dataset(Uploadable, Downloadable):
    def __init__(self, asset_id=None, filepath=None, asset_info=None):
        super(Dataset, self).__init__(asset_id=asset_id, asset_info=asset_info)
        self.filepath = filepath

    def upload(self):
        self._upload(self.filepath, self._info)

    def download(self):
        self._download(self.asset_id)
