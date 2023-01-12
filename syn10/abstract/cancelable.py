import syn10
from syn10.abstract import APIResource


class Cancelable(APIResource):
    def cancel(self):
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/cancel"
        resp = self.request("DELETE", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        return resp.json()
