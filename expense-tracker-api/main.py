from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    amount: int

class Expense(ExpenseCreate):
    id: int

expenses = []
next_id = 1

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Expense Tracker API"}

@app.post("/expenses")
def create_expense(expense: ExpenseCreate):
    global next_id

    new_expense = Expense(
        id = next_id,
        title = expense.title,
        amount = expense.amount
    )

    expenses.append(new_expense)
    next_id += 1

    return new_expense

@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for expense in expenses:
        if expense.id == expense_id:
            return expense
    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, new_expense: ExpenseCreate):
    for expense in expenses:
       if expense.id == expense_id:
           expense.title = new_expense.title
           expense.amount = new_expense.amount
           return expense
    raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    for expense in expenses:
        if expense.id == expense_id:
            expenses.remove(expense)
            return {
                "message": "Expense deleted successfully"
                }

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )