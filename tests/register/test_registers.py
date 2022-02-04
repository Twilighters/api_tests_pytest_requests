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
            res.json().get("message") == ResponseText.MESSAGE_REGISTER_USER
        ), "check response message"
        assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
