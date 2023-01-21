import attr
from faker import Faker
import random
from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AddUserBalanceResponse:
    message: str = attr.ib(default=None)
    balance: int = attr.ib(default=None)


@attr.s
class AddUserBalanceRequest(BaseClass):
    balance: int = attr.ib(default=None)

    @staticmethod
    def random():
        return AddUserBalanceRequest(
            balance=random.randint(20, 99),
        )
