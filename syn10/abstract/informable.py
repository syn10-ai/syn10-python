import syn10
from syn10.abstract import APIResource


class Informable(APIResource):
    @property
    def info(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}"
        resp = self.request("GET", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        return resp.json()
