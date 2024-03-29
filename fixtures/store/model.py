import attr
from faker import Faker
from typing import List
import random

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Store(BaseClass):
    name: str = attr.ib(default=None)

    @staticmethod
    def random():
        return Store(name=fake.first_name().lower() + str(random.randint(0, 9999)))


@attr.s
class StoreResponse:
    name: str = attr.ib()
    uuid: int = attr.ib()
    items: List[str] = attr.ib()
