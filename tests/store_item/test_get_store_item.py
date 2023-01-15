class TestGetStoreItem:
    def test_get_store_item(self, app, store_item):
        """
        1. Try to get store item with valid data
        2. Check the status code is 200
        3. Check response
        """

        res = app.store_item.get_store_item(
            item_name=store_item.store_item_name,
            header=store_item.header,
            type_response=None,
        )
        assert res.status_code == 200, "Check status code"
