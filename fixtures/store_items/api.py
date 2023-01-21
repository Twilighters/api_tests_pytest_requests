from requests import Response

from fixtures.store_items.model import GetStoreItemsResponse
from fixtures.validator import Validator
from common.deco import logging as log


class StoreItemsController(Validator):
    def __init__(self, app):
        self.app = app

    GET_ALL_ITEMS = "/items"

    @log("Get all items of store")
    def get_store_items(
        self, header=None, type_response=GetStoreItemsResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0#/storeItems/itemsGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_ALL_ITEMS}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
