from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from src.core.config import JWT

cookie_transport = CookieTransport(cookie_max_age=36000)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT, lifetime_seconds=36000)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)