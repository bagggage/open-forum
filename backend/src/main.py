import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import question
from src.api.v1 import category
from src.api.v1 import tag
from src.api.v1 import answer
from src.api.v1 import vote
from src.api.v1 import user
from src.api.v1.auth import auth_router

app = FastAPI()

origins = [
    "http://localhost:8080",  
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question.router)
app.include_router(category.router)
app.include_router(tag.router)
app.include_router(answer.router)
app.include_router(vote.router)
app.include_router(user.router)
app.include_router(auth_router)


async def start_api():
    config = uvicorn.Config(app, host='localhost', port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(start_api())

if __name__ == "__main__":
    asyncio.run(main())