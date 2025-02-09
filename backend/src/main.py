from fastapi import FastAPI
from src.api.v1 import question
from src.api.v1 import category

app = FastAPI()

app.include_router(question.router)
app.include_router(category.router)