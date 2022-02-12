from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUserResponse, RegisterUser


class TestAuthUser:
    def test_auth_user_with_valid_data(self, app):
        """
        1. Try to auth user with valid data
        2. Check the status code is 200
        3. Check response
        """

        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert (
            res.json().get("message") == ResponseText.MESSAGE_REGISTER_USER
        ), "check response message"
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
        res_auth = app.auth.login(data=data, type_response=None)
        assert res_auth.status_code == 200, "Check status code"

    def test_auth_user_with_not_registered_user_data(self, app):
        """
        1. Try to auth user with valid data
        2. Check the status code is 200
        3. Check response
        """

        data = RegisterUser.random()
        res = app.auth.login(data=data)
        assert res.status_code == 401, "You login"
