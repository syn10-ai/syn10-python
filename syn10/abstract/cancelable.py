import syn10
from syn10 import utils
from syn10.api_requestor import APIRequestor


class Cancelable:
    @staticmethod
    def get_endpoint():
        raise NotImplementedError

    def get_id(self):
        raise NotImplementedError

    def cancel(self):
        requestor = APIRequestor(token=utils.find_token())
        url = f"{syn10.base}{self.get_endpoint()}/{self.get_id()}/cancel"
        resp = requestor._request("DELETE", url, query={"cls": self.__class__.__name__})
        resp.raise_for_status()
        return resp.json()
