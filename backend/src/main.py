from fastapi import FastAPI
from src.api.v1 import question

app = FastAPI()

app.include_router(question.router)
