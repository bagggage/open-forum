import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from src.main import app
import asyncio

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac

@pytest_asyncio.fixture
async def auth_cookie(async_client):
    test_user_data = {
        "username": "user@example.com",
        "password": "string"
    }
    login_response = await async_client.post(
        "/v1/auth/jwt/login",
        data=test_user_data
    )
    assert login_response.status_code == 204, "Auth error"

    cookie_token = login_response.cookies.get("fastapiusersauth")
    assert cookie_token, "Token cant be taken from cookie"
    
    return {"fastapiusersauth": cookie_token}