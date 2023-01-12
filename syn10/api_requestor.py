from syn10 import utils
from syn10 import error
from syn10 import version

import json
import requests
from requests.exceptions import (
    Timeout
)

TIMEOUT_SECS = 600


class APIRequestor:
    def __init__(self, token: str = None):
        self.token = token or utils.find_token()

    def request(
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
        try:
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
        except Timeout as e:
            raise error.Timeout(str(e)) from e
        if resp.status_code >= 300:
            self._handle_error_response(resp)
        return resp

    def _generate_headers(self, token=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token or self.token}",
            "cache-control": "no-cache",
            "User-Agent": f"Syn10/v1 Python/{version.VERSION}",
        }
        return headers

    def _handle_error_response(self, resp: requests.Response):
        err_code = resp.status_code
        resp_json = resp.json()

        if "error" not in resp_json:
            raise error.InvalidResponse(
                "'error' key is missing.",
                code=err_code
            )

        err_data = resp_json["error"]

        if err_code == 401:
            raise error.AuthenticationError(
                err_data.get("message"),
                code=err_code
            )

