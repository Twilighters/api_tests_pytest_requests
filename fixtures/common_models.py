import attr

from fixtures.base import BaseClass
from fixtures.register.model import RegisterUser
from fixtures.store_item.model import AddStoreItem
from fixtures.user_info.model import AddUserInfo


@attr.s
class MessageResponse:
    message: str = attr.ib()


@attr.s
class UserStore(BaseClass):
    user: RegisterUser = attr.ib(default=None)
    user_uuid: int = attr.ib(default=None)
    header: dict = attr.ib(default=None)
    user_info: AddUserInfo = attr.ib(default=None)
    store_name: str = attr.ib(default=None)
    store_id: int = attr.ib(default=None)
    store_item_info: AddStoreItem = attr.ib(default=None)
    store_item_name: str = attr.ib(default=None)
    user_balance: int = attr.ib(default=None)
    item_id: int = attr.ib(default=None)


@attr.s
class AuthInvalidResponse:
    description: str = attr.ib()
    error: str = attr.ib()
    status_code: int = attr.ib()
