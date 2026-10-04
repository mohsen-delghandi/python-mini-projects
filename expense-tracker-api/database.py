import os
import psycopg
from psycopg.rows import dict_row

def get_connection(dbname):
    return psycopg.connect(
        f"host=localhost dbname={dbname} user=expense_user password=expense_pass",
        row_factory=dict_row
    )

dbname = os.getenv("APP_ENV", "expense_tracker")
conn = get_connection(dbname)

def get_expenses():

    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM expenses"
        )

        rows = cur.fetchall()

    conn.commit()

    return rows

def create_expense(title, amount):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO expenses (title, amount)
            VALUES (%s, %s)
            RETURNING id, title, amount 
            """,
            (title, amount)
        )

        row = cur.fetchone()

    conn.commit()

    return row

def get_expense(expense_id: int):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, title, amount 
            FROM expenses
            WHERE id = %s
            """,
            (expense_id,)
        )

        row = cur.fetchone()

    conn.commit()

    return row

def update_expense(expense_id: int, title: str, amount: str):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE expenses
            SET title = %s, amount = %s
            WHERE id = %s
            RETURNING id, title, amount
            """,
            (
                title,
                amount,
                expense_id)
        )
        row = cur.fetchone()

    conn.commit()

    return row

def delete_expense(expense_id:int):

    with conn.cursor() as cur:

        cur.execute(
            """
            DELETE FROM expenses
            WHERE id = %s
            RETURNING id
            """,
            (expense_id,)
        )

        row = cur.fetchone()

        conn.commit()

    return row

def get_expense_summary():
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT
                title,
                ROUND(AVG(amount)) AS amount_average
            FROM expenses
            GROUP BY title
            HAVING COUNT(*) >= 2
            ORDER BY amount_average DESC
            """
        )

        rows = cur.fetchall()

    return rows