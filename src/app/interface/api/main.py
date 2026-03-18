from fastapi import FastAPI

from vps_deployment.interface.api.routers.notes import router as notes_router

app = FastAPI(title="Notes API", version="1.0.0")

app.include_router(notes_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
