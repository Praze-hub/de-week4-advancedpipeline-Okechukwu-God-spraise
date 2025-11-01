import pytest
from pipeline.api_client import APIClient
from unittest.mock import MagicMock

class FakeResp:
    def __init__(self, data, ok=True):
        self._data = data
        self.ok = ok

    def json(self):
        return self._data

    def raise_for_status(self):
        if not self.ok:
            raise Exception("HTTP error")

def test_get_all_products_pagination(monkeypatch):
    session = MagicMock()
    session.get.side_effect = [
        FakeResp([{"id":1,"title":"a","price":10,"rating":{"count":2},"userId":100}]),
        FakeResp([])
    ]
    client = APIClient("https://fake", session=session)
    products = client.get_all_products(limit=5)
    assert len(products) == 1
    assert session.get.call_count == 2
