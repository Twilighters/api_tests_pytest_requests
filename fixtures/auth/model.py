import attr
from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Auth(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return Auth(username=fake.email(), password=fake.password())


@attr.s
class AuthResponse:
    access_token: str = attr.ib()


@attr.s
class AuthUserType:
    header: dict = attr.ib()
    uuid: int = attr.ib()
