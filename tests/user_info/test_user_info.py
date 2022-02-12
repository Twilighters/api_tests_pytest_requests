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
            user_id=auth_user.uuid, data=data, header=auth_user.header
        )
        assert res.status_code == 200
