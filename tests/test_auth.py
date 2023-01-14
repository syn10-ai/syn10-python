from .fixtures import (
    auth_mock,
    TOKEN
)


def test_get_token(auth_mock):
    assert auth_mock.token == TOKEN
