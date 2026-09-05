from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import (
                        get_expenses,
                        create_expense,
                        get_expense,
                        update_expense,
                        delete_expense
                    )

class ExpenseCreate(BaseModel):
    title: str = Field(min_length=1)
    amount: int = Field(gt=0)

class Expense(ExpenseCreate):
    id: int

app = FastAPI()

def row_to_expense(row):
    return Expense(
        id=row["id"],
        title=row["title"],
        amount=row["amount"]
    )

@app.get("/")
def home():
    return {"message": "Expense Tracker API"}

@app.post("/expenses", response_model = Expense, status_code=201)
def create_expense_endpoint(expense: ExpenseCreate):

    row = create_expense(
        expense.title,
        expense.amount
    )

    return row_to_expense(row)

@app.get("/expenses", response_model = list[Expense])
def get_all_expenses():
    expenses = get_expenses()
    expenses_list = [
        row_to_expense(expense)
        for expense in expenses
    ]

    return expenses_list

@app.get("/expenses/{expense_id}", response_model=Expense)
def get_expense_endpoint(expense_id: int):
    row = get_expense(expense_id)

    if row is None:
        raise HTTPException(
                status_code=404,
                detail="Expense not found"
            )

    return row_to_expense(row)

@app.put("/expenses/{expense_id}", response_model = Expense)
def update_expense_endpoint(expense_id: int, new_expense: ExpenseCreate):
    row = update_expense(
        expense_id,
        new_expense.title,
        new_expense.amount
    )

    if row is None:
        raise HTTPException(
                status_code=404,
                detail="Expense not found"
            )

    return row_to_expense(row)

@app.delete("/expenses/{expense_id}")
def delete_expense_endpoint(expense_id: int):

    row = delete_expense(expense_id)

    if row is None:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {"id": row["id"]}