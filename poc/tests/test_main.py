import pytest
from fastapi.testclient import TestClient
from poc.src.main import app

client = TestClient(app)


@pytest.mark.parametrize("expected_status_code", [200])
def test_get_all_users(expected_status_code):
    response = client.get("/users")
    print(response.status_code)
    assert response.status_code == expected_status_code
    if expected_status_code == 200:
        users = response.json()
        assert len(users) > 0
