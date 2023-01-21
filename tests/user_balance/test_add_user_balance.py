from fixtures.user_balance.model import AddUserBalanceRequest


class TestAddUserBalance:
    def test_add_user_balance(self, app, store_item):
        """
        1. Try to add user balance with valid data
        2. Check the status code is 200
        3. Check response
        """

        data = AddUserBalanceRequest().random()
        data.store_id = store_item.store_id
        res = app.user_balance.add_user_balance(
            user_id=store_item.user_uuid, data=data, header=store_item.header
        )
        assert res.status_code == 201, "Check status code"
