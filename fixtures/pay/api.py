from requests import Response

from fixtures.pay.model import PayItemRequest, PayItemResponse
from fixtures.validator import Validator
from common.deco import logging as log


class PayController(Validator):
    def __init__(self, app):
        self.app = app

    POST_PAY = "/pay/{}"

    @log("Pay item")
    def pay_item(
        self,
        user_id: int,
        data: PayItemRequest,
        header=None,
        type_response=PayItemResponse,
    ) -> Response:
        """
        https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0#/pay/pay # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_PAY.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
