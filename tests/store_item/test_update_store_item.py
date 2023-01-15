from fixtures.store_item.model import UpdateStoreItem


class TestUpdateStoreItem:
    def test_update_store_item(self, app, user_info, store_item):
        """
        1. Try to update store item with valid data
        2. Check the status code is 200
        3. Check response
        """

        data = UpdateStoreItem().random()
        res = app.store_item.update_store_item(
            item_name=store_item.store_item_name,
            data=data,
            header=user_info.header,
            type_response=None,
        )
        assert res.status_code == 200, "Check status code"
