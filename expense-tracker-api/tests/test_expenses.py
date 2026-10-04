from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_expense():
    response = client.post(
        "/expenses",
        json = {
            "title": "Gas",
            "amount": 800000
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Gas"
    assert response.json()["amount"] == 800000

def test_get_expense():
    expense = client.post(
        "/expenses",
        json = {
            "title": "Gas",
            "amount": 800000
        }
    )

    response = client.get(
        f"/expenses/{expense.json()['id']}"
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Gas"
    assert response.json()["amount"] == 800000

def test_update_expense():
    expense = client.post(
        "/expenses",
        json = {
            "title": "Gas",
            "amount": 800000
        }
    )

    response = client.put(
        f"/expenses/{expense.json()['id']}",
        json = {
                    "title": "Book",
                    "amount": 900000
                }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Book"
    assert response.json()["amount"] == 900000

def test_delete_expense():
    expense = client.post(
            "/expenses",
            json = {
                "title": "Gas",
                "amount": 800000
            }
        )

    response = client.delete(
        f"/expenses/{expense.json()['id']}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == expense.json()["id"]

def test_get_all_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Gas",
            "amount": 800000
        }
    )

    client.post(
        "/expenses",
        json={
            "title": "Book",
            "amount": 900000
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_expense_not_found():
    response = client.get("/expenses/999999")

    assert response.status_code == 404

def test_delete_expense_not_found():
    response = client.delete("/expenses/999999")

    assert response.status_code == 404

def test_create_expense_invalid_amount():
    response = client.post(
        "/expenses",
        json={
            "title": "Gas",
            "amount": -100
        }
    )

    assert response.status_code == 422

def test_create_expense_empty_title():
    response = client.post(
        "/expenses",
        json={
            "title": "",
            "amount": 800000
        }
    )

    assert response.status_code == 422

def test_expense_summary():
    client.post(
        "/expenses",
        json={"title": "Gas", "amount": 800000}
    )

    client.post(
        "/expenses",
        json={"title": "Gas", "amount": 900000}
    )

    client.post(
        "/expenses",
        json={"title": "Book", "amount": 1000000}
    )

    response = client.get("/expenses/summary")

    print(response.json())

    assert response.status_code == 200
    assert response.json()[0]["title"] == "Gas"
    assert response.json()[0]["amount_average"] == 850000