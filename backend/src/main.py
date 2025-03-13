import asyncio
import uvicorn
from fastapi import FastAPI
from src.api.v1 import question
from src.api.v1 import category
from src.api.v1 import tag
from src.api.v1 import answer
from src.api.v1 import vote
from src.api.v1.auth import auth_router

app = FastAPI()

app.include_router(question.router)
app.include_router(category.router)
app.include_router(tag.router)
app.include_router(answer.router)
app.include_router(vote.router)
app.include_router(auth_router)


async def start_api():
    config = uvicorn.Config(app, host='localhost', port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(start_api())

if __name__ == "__main__":
    asyncio.run(main())