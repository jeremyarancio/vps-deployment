from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.application.exceptions import ApplicationException
from app.infrastructure.notes import InMemoryNoteRepository
from app.interface.api.routers.notes import router as notes_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    InMemoryNoteRepository.init()
    yield


app = FastAPI(title="Notes API", version="1.0.0", lifespan=lifespan)


@app.exception_handler(ApplicationException)
def application_exception_handler(
    request: Request, exc: ApplicationException
) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.exception_handler(Exception)
def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=500, content={"detail": "Internal server error."})


app.include_router(notes_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
