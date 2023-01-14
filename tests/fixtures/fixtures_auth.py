import pytest
import requests_mock

from .fixtures_globals import (
    BASE,
    CLIENT_ID,
    CLIENT_SECRET,
    TOKEN
)

from ..context import Auth


@pytest.fixture()
def auth_mock(requests_mock):
    url_get_token = f"{BASE}/oauth/token"
    json_get_token = {
        "access_token": TOKEN,
        "token_type": "Bearer"
    }
    requests_mock.post(url_get_token, json=json_get_token)

    auth = Auth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    return auth
