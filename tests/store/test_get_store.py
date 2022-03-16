# from fixtures.store.model import Store, StoreResponse


class TestGetStore:
    def test_get_store(self, app, store):
        """
        1. Try to get store
        2. Check the status code is 200
        3. Check response
        """
        res = app.store.get_store(store.store, header=store.header)
        assert res.status_code == 200, "Check status code"
