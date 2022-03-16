# from fixtures.common_models import AuthInvalidResponse
from fixtures.store.model import Store


class TestAddStore:
    def test_add_store_with_valid_data(self, app, user_info):
        """
        1. Try add store with valid data
        2. Check the status code is 201
        3. Check response
        """
        data = Store.random()
        res = app.store.add_store(data.name, header=user_info.header)
        assert res.status_code == 201, "Check status code"
        assert res.data.name == data.name

    # TODO отрефакторить код ниже, а то тест не работает
    # def test_add_store_without_header(self, app, user_info):
    #     """
    #     1. Try to add store without auth header
    #     2. Check that status code is 401
    #     3. Check response
    #     """
    #     data = Store.random()
    #     res = app.store.add_store(
    #         name=data.name,
    #         header=None,
    #         type_response=AuthInvalidResponse
    #     )
    #     assert res.status_code == 401, "check status code"

    # def test_add_user_info_invalid_token(self, app, auth_user, user_info):
    #     """
    #     1. Try to add user info with invalid token
    #     2. Check the status code is 401
    #     3. Check response
    #     """
    #
    #     data = AddUserInfo.random()
    #     res = app.user_info.add_user_info(
    #         user_id=user_info.user_uuid,
    #         data=data,
    #         type_response=None,
    #         header={"Authorization": f"JWT {1231231}"},
    #     )
    #     assert res.status_code == 401
    #
    # def test_update_user_with_none_exist_user_id(
    #     self, app, auth_user, user_info, none_exist_user_id=99999
    # ):
    #     """
    #     1. Try to update user info with none exist user id
    #     2. Check the status code is 404
    #     3. Check response
    #     """
    #
    #     data = AddUserInfo.random()
    #     res = app.user_info.add_user_info(
    #         user_id=none_exist_user_id,
    #         data=data,
    #         type_response=None,
    #         header=auth_user.header,
    #     )
    #     assert res.status_code == 404
