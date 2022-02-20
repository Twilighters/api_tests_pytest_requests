class TestDeleteUserInfo:
    def test_delete_user_info(self, app, user_info):
        """
        1. Try to delete user info with valid data
        2. Check the status code is 200
        3. Check response
        """

        res = app.user_info.delete_user_info(
            user_id=user_info.user_uuid, header=user_info.header
        )
        assert res.status_code == 200

    def test_delete_user_info_none_exist_user_id(
        self, app, user_info, none_exist_user_id=99999
    ):
        """
        1. Try to delete user info with none exist user id
        2. Check the status code is 404
        3. Check response
        """

        res = app.user_info.delete_user_info(
            user_id=none_exist_user_id, type_response=None, header=user_info.header
        )
        assert res.status_code == 404

    def test_delete_user_info_without_header(self, app, auth_user, user_info):
        """
        1. Try to delete user info without header
        2. Check the status code is 401
        3. Check response
        """

        res = app.user_info.delete_user_info(
            user_id=user_info.user_uuid, type_response=None, header=None
        )
        assert res.status_code == 401
