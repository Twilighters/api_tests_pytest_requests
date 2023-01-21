import logging

import pytest

from fixtures.app import StoreApp
from fixtures.register.model import RegisterUser
from fixtures.common_models import UserStore
from fixtures.store_item.model import AddStoreItem, ItemName
from fixtures.user_balance.model import AddUserBalanceRequest
from fixtures.user_info.model import AddUserInfo
from fixtures.store.model import Store

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return StoreApp(url)


@pytest.fixture
def register_user(app) -> UserStore:
    """
    Register new user
    """
    data = RegisterUser.random()
    res = app.register.register_new_user(data=data)
    data = UserStore(user=data, user_uuid=res.data.uuid)
    return data


@pytest.fixture
def auth_user(app, register_user) -> UserStore:
    """
    Login user
    """
    res = app.auth.login(data=register_user.user)
    token = res.data.access_token
    header = {"Authorization": f"JWT {token}"}
    data = UserStore(**register_user.to_dict())
    data.header = header
    return data


@pytest.fixture
def user_info(app, auth_user) -> UserStore:
    """
    Add user info
    """
    data = AddUserInfo.random()
    app.user_info.add_user_info(
        user_id=auth_user.user_uuid, data=data, header=auth_user.header
    )
    data_user = UserStore(**auth_user.to_dict())
    data_user.user_info = data
    return data_user


@pytest.fixture
def get_store_name(app, user_info) -> UserStore:
    """
    Add store
    """
    data = Store.random()
    res = app.store.add_store(data.name, header=user_info.header)
    user_info.store_id = res.data.uuid
    user_info.store_name = res.data.name
    return user_info


@pytest.fixture
def store_item(app, user_info) -> UserStore:
    """
    Get store item id
    """
    item_name = ItemName.random()
    data = AddStoreItem().random()
    data.store_id = user_info.store_id
    res = app.store_item.add_store_item(
        item_name=item_name.item_name, data=data, header=user_info.header
    )
    user_info = UserStore(**user_info.to_dict())
    user_info.store_item_name = item_name.item_name
    user_info.item_id = res.data.itemID
    return user_info


@pytest.fixture
def user_balance(app, store_item) -> UserStore:
    """
    Add user balance
    """
    data = AddUserBalanceRequest().random()
    data.store_id = store_item.store_id
    res = app.user_balance.add_user_balance(
        user_id=store_item.user_uuid, data=data, header=store_item.header
    )
    store_item.user_balance = res.data.balance
    return store_item


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="http://localhost:56733",
    ),
