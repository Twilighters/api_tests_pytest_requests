import logging

import pytest

from fixtures.app import StoreApp
from fixtures.auth.model import AuthResponse, AuthUserType
from fixtures.register.model import RegisterUser, RegisterUserResponse

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    # Todo: Add logger
    return StoreApp(url)


@pytest.fixture()
def auth_user(app):
    data = RegisterUser.random()
    res_register = app.register.register(data=data, type_response=RegisterUserResponse)
    res_auth = app.auth.login(data=data, type_response=AuthResponse)
    token = res_auth.data.access_token
    user_uuid = res_register.data.uuid
    header = {"Authorization": f"JWT {token}"}
    return AuthUserType(header, user_uuid)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),
