from typing import Optional

import os
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


class Auth:
    def __init__(
            self,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self._get_token()

    def _get_token(self):
        client = BackendApplicationClient(
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        token_session = OAuth2Session(client=client)
        token_response = token_session.fetch_token(
            token_url="http://127.0.0.1:8000/oauth/token",
            auth=auth
        )
        return token_response['access_token']

