from fixtures.store_item.model import AddStoreItem, ItemName


class TestAddStoreItem:
    def test_add_store_item(self, app, user_info):
        """
        1. Try to add user info with valid data
        2. Check the status code is 200
        3. Check response
        """
        item_name = ItemName.random()
        data = AddStoreItem().random()
        data.store_id = user_info.store_id
        res = app.store_item.add_store_item(
            item_name=item_name.item_name,
            data=data,
            header=user_info.header,
            type_response=None,
        )
        assert res.status_code == 201, "Check status code"
