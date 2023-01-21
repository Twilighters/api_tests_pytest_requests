from fixtures.auth.api import AuthController
from fixtures.pay.api import PayController
from fixtures.register.api import RegisterController
from fixtures.store.api import StoreMagazineController
from fixtures.store_item.api import StoreItemController
from fixtures.store_items.api import StoreItemsController
from fixtures.user_balance.api import UserBalanceController
from fixtures.user_info.api import UserInfoController
from fixtures.requests import Client


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = RegisterController(self)
        self.auth = AuthController(self)
        self.user_info = UserInfoController(self)
        self.store = StoreMagazineController(self)
        self.store_item = StoreItemController(self)
        self.store_items = StoreItemsController(self)
        self.user_balance = UserBalanceController(self)
        self.pay = PayController(self)
