from fastapi import FastAPI
from src.api.v1 import question
from src.api.v1 import category
from src.api.v1 import tag
from src.api.v1 import answer

app = FastAPI()

app.include_router(question.router)
app.include_router(category.router)
app.include_router(tag.router)
app.include_router(answer.router)