from fastapi import FastAPI
from database import init_db
from contextlib import asynccontextmanager
from routers import search

#anything that runs before yield runs on startup, anything after on shutdown.
@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(search.router)