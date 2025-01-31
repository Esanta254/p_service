

import pytest
from unittest.mock import patch
from app.middleware import jwt


@pytest.fixture
def authenticated_client(client):
    """Fixture to simulate an authenticated client."""
    with patch("app.middleware.jwt.decode") as mock_decode:
        mock_decode.return_value = {
            "sub": "auth0|1234567890",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "scope": "create:customer"
        }
        yield client

def test_add_customer(authenticated_client):
    response = authenticated_client.post('/customers', json={
        "name": "John Doe",
        "code": "CUST123",
        "phone": "+254700000000"
    })
    assert response.status_code == 201
    assert response.json['message'] == "Customer added successfully"

def test_add_customer_missing_fields(authenticated_client):
    response = authenticated_client.post('/customers', json={
        "name": "John Doe"
    })
    assert response.status_code == 400
    assert "error" in response.json
