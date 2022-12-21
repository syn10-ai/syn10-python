__all__ = [
    "authenticate"
]

from typing import Optional
from syn10.auth import Auth

_auth: Optional[Auth] = None


def authenticate(
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None
):
    global _auth
    _auth = Auth(
        client_id=client_id,
        client_secret=client_secret
    )




