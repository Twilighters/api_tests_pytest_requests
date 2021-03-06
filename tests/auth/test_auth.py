from fixtures.auth.model import Auth
from fixtures.common_models import AuthInvalidResponse
from fixtures.constants import ResponseText


class TestAuthUser:
    def test_auth_user_with_valid_data(self, app, register_user):
        """
        1. Try to auth user with valid data
        2. Check the status code is 200
        3. Check response
        """

        res = app.auth.login(data=register_user.user)
        assert res.status_code == 200, "You are not login"

    def test_auth_user_with_not_registered_user_data(self, app):
        """
        1. Try to auth user with not registered user data
        2. Check the status code is 401
        3. Check response
        """

        data = Auth.random()
        res = app.auth.login(data=data, type_response=AuthInvalidResponse)
        assert res.status_code == 401, "You are login"
        assert res.data.description == ResponseText.DESCRIPTION_AUTH
        assert res.data.error == ResponseText.ERROR_AUTH
        assert res.data.status_code == 401
