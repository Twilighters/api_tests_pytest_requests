from requests import Response
from fixtures.user_info.model import AddUserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USER_INFO = "/user_info/{}"

    @log("Add user info")
    def add_user_info(
        self, user_id: int, data: AddUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfoAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
