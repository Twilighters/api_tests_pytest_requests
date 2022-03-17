from fixtures.common_models import AuthInvalidResponse, MessageResponse
from fixtures.constants import ResponseText


class TestGetUserInfo:
    def test_get_user_info(self, app, user_info):
        """
        1. Try to get user info with valid data
        2. Check the status code is 200
        3. Check response
        """

        res = app.user_info.get_user_info(
            user_id=user_info.user_uuid, header=user_info.header
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.city == user_info.user_info.address.city, "Check city"
        assert res.data.street == user_info.user_info.address.street, "Check street"
        assert res.data.email == user_info.user_info.email, "Check email"

    def test_get_user_info_none_exist_user_id(
        self, app, user_info, none_exist_user_id=99999
    ):
        """
        1. Try to get user info with none exist user id
        2. Check the status code is 404
        3. Check response
        """

        res = app.user_info.get_user_info(
            user_id=none_exist_user_id,
            type_response=MessageResponse,
            header=user_info.header,
        )
        assert res.status_code == 404, "check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND

    def test_get_user_info_without_header(self, app, auth_user, user_info):
        """
        1. Try to get user info without header
        2. Check the status code is 401
        3. Check response
        """

        res = app.user_info.get_user_info(
            user_id=user_info.user_uuid, type_response=AuthInvalidResponse, header=None
        )
        assert res.status_code == 401, "Check status code"
        assert res.data.description == ResponseText.DESCRIPTION_AUTH_ERROR
        assert res.data.error == ResponseText.ERROR_AUTH_TEXT
        assert res.data.status_code == 401, "Check status code"
