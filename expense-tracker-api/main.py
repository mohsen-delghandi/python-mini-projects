from fastapi import FastAPI
from routers.expenses import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Expense Tracker API"}

