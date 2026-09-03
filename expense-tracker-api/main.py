from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import (
                        get_expenses,
                        create_expense,
                        get_expense,
                        update_expense,
                        delete_expense
                    )

class ExpenseCreate(BaseModel):
    title: str
    amount: int

class Expense(ExpenseCreate):
    id: int

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Expense Tracker API"}

@app.post("/expenses")
def create_expense_endpoint(expense: ExpenseCreate):

    row = create_expense(
        expense.title,
        expense.amount
    )

    return {
        "id": row[0],
        "title": row[1],
        "amount": row[2]
    }

@app.get("/expenses")
def get_all_expenses():
    return get_expenses()

@app.get("/expenses/{expense_id}")
def get_expense_endpoint(expense_id: int):
    row = get_expense(expense_id)

    if row is None:
        raise HTTPException(
                status_code=404,
                detail="Expense not found"
            )

    return {
        "id": row[0],
        "title": row[1],
        "amount": row[2]
    }

@app.put("/expenses/{expense_id}")
def update_expense_endpoint(expense_id: int, new_expense: ExpenseCreate):
    row = update_expense(expense_id,new_expense.title, new_expense.amount)

    if row is None:
        raise HTTPException(
                status_code=404,
                detail="Expense not found"
            )

    return {
            "id": row[0],
            "title": row[1],
            "amount": row[2]
    }

@app.delete("/expenses/{expense_id}")
def delete_expense_endpoint(expense_id: int):

    row = delete_expense(expense_id)

    if row is None:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {"id": row[0]}