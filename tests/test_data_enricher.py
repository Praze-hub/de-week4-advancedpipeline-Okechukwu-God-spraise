import pandas as pd
from pipeline.data_enricher import DataEnricher
import pytest

@pytest.fixture
def sample_products():
    return [
        {"id": 1, "title": "P1", "price": 10, "rating": {"count": 2}, "userId": 101},
        {"id": 2, "title": "P2", "price": 5, "rating": {"count": 1}, "userId": 999},  # missing user
    ]

@pytest.fixture
def sample_users():
    return [
        {"id": 101, "username": "alice", "email": "alice@example.com", "name": {"firstname":"Alice","lastname":"A"}},
    ]

def test_enrich_success_and_missing_user(sample_products, sample_users):
    enr = DataEnricher()
    df = enr.enrich(sample_products, sample_users)
    assert df.loc[df["id"]==1, "seller_username"].iloc[0] == "alice"
    assert pd.isna(df.loc[df["id"]==2, "seller_username"].iloc[0])
    assert df.loc[df["id"]==1, "revenue"].iloc[0] == 20

def test_revenue_calculation(sample_products, sample_users):
    enr = DataEnricher()
    df = enr.enrich(sample_products, sample_users)
    assert df["revenue"].tolist() == [20, 5]  # second: 5 * 1
