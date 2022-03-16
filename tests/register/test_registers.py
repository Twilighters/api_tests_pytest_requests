import pytest

from fixtures.common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse


class TestRegisterUser:
    def test_register_user_with_valid_data(self, app):
        """
        1. Try register user with valid data
        2. Check the status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert (
            res.data.message == ResponseText.MESSAGE_REGISTER_USER
        ), "check response message"

    @pytest.mark.parametrize("field", ["username", "password"])
    def test_register_user_with_empty_data(self, app, field):
        """
        1. Try register user with invalid data
        2. Check the status code is 400
        3. Check response
        """
        data = RegisterUser.random()
        setattr(data, field, None)
        res = app.register.register(data=data, type_response=MessageResponse)
        assert res.status_code == 400, "check status code"
        assert (
            res.data.message == ResponseText.MESSAGE_USER_PASSWORD_REQUIRED
        ), "check response message"
