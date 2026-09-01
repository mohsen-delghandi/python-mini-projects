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

    assert response.status_code == 200
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
    assert response.json()["message"] == "Expense deleted successfully"