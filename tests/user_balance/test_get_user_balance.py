class TestGetUserBalance:
    def test_get_user_balance(self, app, user_balance):
        """
        1. Try to get user balance item with valid data
        2. Check the status code is 200
        3. Check response
        """

        res = app.user_balance.get_user_balance(
            user_id=user_balance.user_uuid, header=user_balance.header
        )
        assert res.status_code == 200, "Check status code"
