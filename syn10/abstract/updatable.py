import syn10
from syn10.abstract import APIResource


class Updatable(APIResource):
    def update(self, **params):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}"
        resp = self.request("PUT", url, data=params, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        return resp
