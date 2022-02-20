import pytest

from fixtures.user_info.model import AddUserInfo


class TestAddUserInfo:
    def test_add_user_info(self, app, auth_user):
        """
        1. Try to add user info with valid data
        2. Check the status code is 200
        3. Check response
        """

        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=auth_user.user_uuid, data=data, header=auth_user.header
        )
        assert res.status_code == 200

    @pytest.mark.parametrize("uuid", ["string", "@", -55, True])
    def test_add_invalid_id_user_info(self, app, auth_user, user_info, uuid):
        """
        1. Try to add user info with invalid user id
        2. Check the status code is 404
        3. Check response
        """

        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=uuid, data=data, type_response=None, header=auth_user.header
        )
        assert res.status_code == 404

    @pytest.mark.xfail(reason="expected error 404")
    def test_add_invalid_phone_user_info(
        self, app, auth_user, user_info, phone="1" * 100
    ):
        """
        1. Try to add user info with invalid phone data
        2. Check the status code is 404
        3. Check response
        """

        data = AddUserInfo.random()
        setattr(data, "phone", phone)
        res = app.user_info.add_user_info(
            user_id=user_info.user_uuid,
            data=data,
            type_response=None,
            header=auth_user.header,
        )
        assert res.status_code == 404

    def test_add_user_info_without_header(self, app, auth_user, user_info):
        """
        1. Try to update user info without header
        2. Check the status code is 401
        3. Check response
        """

        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=user_info.user_uuid, data=data, type_response=None, header=None
        )
        assert res.status_code == 401

    def test_add_user_info_invalid_token(self, app, auth_user, user_info):
        """
        1. Try to add user info with invalid token
        2. Check the status code is 401
        3. Check response
        """

        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=user_info.user_uuid,
            data=data,
            type_response=None,
            header={"Authorization": f"JWT {1231231}"},
        )
        assert res.status_code == 401

    def test_update_user_with_none_exist_user_id(
        self, app, auth_user, user_info, none_exist_user_id=99999
    ):
        """
        1. Try to update user info with none exist user id
        2. Check the status code is 404
        3. Check response
        """

        data = AddUserInfo.random()
        res = app.user_info.add_user_info(
            user_id=none_exist_user_id,
            data=data,
            type_response=None,
            header=auth_user.header,
        )
        assert res.status_code == 404
