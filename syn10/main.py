__all__ = [
    "authenticate"
]

from typing import Optional
from syn10.auth import Auth

_auth: Optional[Auth] = None


def authenticate(client_id: str, client_secret: str):
    global _auth
    _auth = Auth(
        client_id=client_id,
        client_secret=client_secret
    )




