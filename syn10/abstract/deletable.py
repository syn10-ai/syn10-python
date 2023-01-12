import syn10
from syn10.abstract import APIResource


class Deletable(APIResource):
    def delete(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/delete"
        resp = self.request("DELETE", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        return resp.json()
