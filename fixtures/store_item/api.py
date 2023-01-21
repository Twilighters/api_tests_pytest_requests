from requests import Response

from fixtures.store_item.model import GetStoreItemResponse
from fixtures.user_info.model import AddUserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class StoreItemController(Validator):
    def __init__(self, app):
        self.app = app

    POST_ITEM = "/item/{}"
    PUT_ITEM = "/item/{}"
    GET_ITEM = "/item/{}"

    @log("Add item to store")
    def add_store_item(
        self,
        item_name: int,
        data: AddUserInfo,
        header=None,
        type_response=GetStoreItemResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/itemAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_ITEM.format(item_name)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Update item from store")
    def update_store_item(
        self,
        item_name: str,
        data: AddUserInfo,
        header=None,
        type_response=GetStoreItemResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/itemChange # noqa
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_ITEM.format(item_name)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get item from store")
    def get_store_item(
        self, item_name: str, header=None, type_response=GetStoreItemResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeItem/itemGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_ITEM.format(item_name)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
