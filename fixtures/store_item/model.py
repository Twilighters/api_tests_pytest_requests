import attr
from faker import Faker
import random
from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AddStoreItem(BaseClass):
    price: str = attr.ib(default=None)
    store_id: int = attr.ib(default=None)
    description: str = attr.ib(default=None)
    image: str = attr.ib(default=None)

    @staticmethod
    def random():
        return AddStoreItem(
            price=fake.random_digit_not_null(),
            store_id=fake.random_digit_not_null(),
            description=fake.text(max_nb_chars=20),
            image=fake.file_extension(category="image"),
        )


@attr.s
class UpdateStoreItem(BaseClass):
    price: str = attr.ib(default=None)
    store_id: int = attr.ib(default=None)
    description: str = attr.ib(default=None)
    image: str = attr.ib(default=None)

    @staticmethod
    def random():
        return AddStoreItem(
            price=fake.random_digit_not_null(),
            store_id=fake.random_digit_not_null(),
            description=fake.text(max_nb_chars=20),
            image=fake.file_extension(category="image"),
        )


@attr.s
class ItemName(BaseClass):
    item_name: str = attr.ib(default=None)

    @staticmethod
    def random():
        return ItemName(
            item_name=fake.first_name().lower() + str(random.randint(1, 9999)),
        )


@attr.s
class GetStoreItemResponse:
    name: str = attr.ib(default=None)
    price: int = attr.ib(default=None)
    itemID: int = attr.ib(default=None)
    description: str = attr.ib(default=None)
    image: str = attr.ib(default=None)
