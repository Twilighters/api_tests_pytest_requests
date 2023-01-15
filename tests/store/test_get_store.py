from fixtures.constants import ResponseText
from fixtures.store.model import Store
from fixtures.common_models import MessageResponse


class TestGetStore:
    def test_get_store(self, app, get_store_name):
        """
        1. Try to get store
        2. Check the status code is 200
        3. Check response
        """
        res = app.store.get_store(
            name=get_store_name.store_name, header=get_store_name.header
        )
        assert res.status_code == 200, "Check status code"

    def test_get_store_with_none_exist_name(self, app, user_info):
        """
        1. Try to get store with none exist name
        2. Check that status code is 404
        3. Check response
        """
        data = Store("Test12345")
        res = app.store.get_store(
            data.name, header=user_info.header, type_response=MessageResponse
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_STORE_NOT_FOUND
