import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from services.agent_service import criar_cliente
from routers import chat

@asynccontextmanager
async def lifespan(app):
    app.state.client = await criar_cliente().__aenter__()
    yield
    await app.state.client.__aexit__(None, None, None)

app = FastAPI(lifespan=lifespan)
app.include_router(chat.router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
