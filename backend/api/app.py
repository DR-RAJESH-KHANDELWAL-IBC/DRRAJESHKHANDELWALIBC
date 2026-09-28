"""
👑 DR RAJESH KHANDELWAL IBC 👑

Main FastAPI application.
SUPREME + ADMIN + OWNER
Central Hub: SUPREMESETUHUB
"""

from fastapi import FastAPI

from backend.api.supreme import router as supreme_router
from backend.metadata import get_backend_metadata
from backend.api.hub import router as hub_router


app = FastAPI(
    title="👑 DR RAJESH KHANDELWAL IBC 👑",
    description="SUPREME ADMIN OWNER API",
    version="1.0.0",
)

# Register Supreme API
app.include_router(supreme_router)
app.include_router(hub_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to DR RAJESH KHANDELWAL IBC",
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
        "repository": "DRRAJESHKHANDELWALIBC",
        "central_hub": "SUPREMESETUHUB",
        "status": "active",
    }


@app.get("/health")
def health_check():
    return {
        "success": True,
        "status": "healthy",
        "repository": "DRRAJESHKHANDELWALIBC",
    }


@app.get("/metadata")
def metadata():
    return get_backend_metadata()
