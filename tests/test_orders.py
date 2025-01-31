

from app.middleware import jwt

def test_add_order(authenticated_client):
    # Add a customer first
    authenticated_client.post('/customers', json={
        "name": "John Doe",
        "code": "CUST123",
        "phone": "+254700000000"
    })
    # Add an order
    response = authenticated_client.post('/orders', json={
        "customer_id": 1,
        "item": "Laptop",
        "amount": 1200.00
    })
    assert response.status_code == 201
    assert response.json['message'].startswith("Order added successfully")
