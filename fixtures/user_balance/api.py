from requests import Response

from fixtures.store_item.model import GetStoreItemResponse
from fixtures.user_balance.model import AddUserBalanceRequest, AddUserBalanceResponse
from fixtures.validator import Validator
from common.deco import logging as log


class UserBalanceController(Validator):
    def __init__(self, app):
        self.app = app

    POST_BALANCE = "/balance/{}"
    GET_BALANCE = "/balance/{}"

    @log("Add user balance")
    def add_user_balance(
        self,
        user_id: int,
        data: AddUserBalanceRequest,
        header=None,
        type_response=AddUserBalanceResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0#/userBalance/balanceAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_BALANCE.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @log("Get user balance")
    def get_user_balance(
        self, user_id: int, header=None, type_response=GetStoreItemResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0#/userBalance/balanceGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_BALANCE.format(user_id)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)
