from fixtures.pay.model import PayItemRequest


class TestPayItem:
    def test_pay_item(self, app, user_balance):
        """
        1. Try to pay item with valid data
        2. Check the status code is 200
        3. Check response
        """

        data = PayItemRequest()
        data.itemId = user_balance.item_id
        res = app.pay.pay_item(
            user_id=user_balance.user_uuid, data=data, header=user_balance.header
        )
        assert res.status_code == 200, "Check status code"
