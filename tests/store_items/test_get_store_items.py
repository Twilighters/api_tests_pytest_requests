class TestGetStoreItem:
    def test_get_store_items(self, app, store_item):
        """
        1. Try to get store items with valid data
        2. Check the status code is 200
        3. Check response
        """

        res = app.store_items.get_store_items(header=store_item.header)
        assert res.status_code == 200, "Check status code"
