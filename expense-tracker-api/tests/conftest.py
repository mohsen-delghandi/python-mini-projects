import pytest
from database import get_connection


@pytest.fixture(autouse=True)
def clean_database():
    conn = get_connection("expense_tracker_test")

    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE expenses RESTART IDENTITY")

    conn.commit()
    conn.close()