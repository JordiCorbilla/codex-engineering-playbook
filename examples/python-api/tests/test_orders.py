from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_and_get_order() -> None:
    create_response = client.post(
        "/orders",
        json={"customer_name": "Acme Corp", "total_amount": 42.5},
    )
    assert create_response.status_code == 201
    created = create_response.json()

    get_response = client.get(f"/orders/{created['id']}")
    assert get_response.status_code == 200
    fetched = get_response.json()

    assert fetched["customer_name"] == "Acme Corp"
    assert fetched["total_amount"] == 42.5


def test_get_missing_order_returns_404() -> None:
    response = client.get("/orders/missing-order")
    assert response.status_code == 404
    assert response.json()["detail"] == "Order 'missing-order' was not found."
