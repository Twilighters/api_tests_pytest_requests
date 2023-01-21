import attr
from faker import Faker
from fixtures.base import BaseClass

fake = Faker()


@attr.s
class PayItemResponse:
    message: str = attr.ib(default=None)
    balance: int = attr.ib(default=None)
    name: str = attr.ib(default=None)
    price: int = attr.ib(default=None)


@attr.s
class PayItemRequest(BaseClass):
    itemId: int = attr.ib(default=None)
