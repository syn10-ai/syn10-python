import json
import requests
from syn10 import utils
from syn10 import version

TIMEOUT_SECS = 600


class APIRequestor:
    def __init__(self, token: str = None):
        self.token = token or utils.find_token()

    def _generate_headers(self, token=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token or self.token}",
            "cache-control": "no-cache",
            "User-Agent": f"Syn10/v1 Python/{version.VERSION}",
        }
        return headers

    def _request(
            self,
            method,
            url,
            *,
            token=None,
            query=None,
            data=None,
            headers={},
            files=None,
            timeout=TIMEOUT_SECS,
            verify=False,
            stream=False
    ):
        _headers = self._generate_headers(token=token)
        _headers.update(headers)
        resp = requests.request(
            method,
            url,
            params=query,
            data=json.dumps(data),
            headers=_headers,
            files=files,
            timeout=timeout,
            verify=verify,
            stream=stream
        )

        resp.raise_for_status()
        return resp
