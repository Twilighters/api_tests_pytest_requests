import attr
from faker import Faker

fake = Faker()


@attr.s
class GetStoreItemsResponse:
    name: str = attr.ib(default=None)
    price: int = attr.ib(default=None)
    itemID: int = attr.ib(default=None)
    description: str = attr.ib(default=None)
    image: str = attr.ib(default=None)
