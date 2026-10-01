"""
👑 DR RAJESH KHANDELWAL IBC 👑

Main FastAPI application.
SUPREME + ADMIN + OWNER

Central Hub:
SUPREMESETUHUB
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.api.supreme import router as supreme_router
from backend.api.hub import router as hub_router
from backend.api.repositories import router as repositories_router
from backend.metadata import get_backend_metadata


# ============================================================
# APPLICATION
# ============================================================

app = FastAPI(
    title="👑 DR RAJESH KHANDELWAL IBC 👑",
    description="SUPREME ADMIN OWNER API",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

ALLOWED_ORIGINS = [
    # GitHub Pages
    "https://rajeshkhandelwal.github.io",
    "https://rajeshkhandelwalofficial.github.io",
    "https://drrajeshkhandelwalibc.github.io",
    "https://drrajeshkhandelwalibcofficial.github.io",

    # Main Domains
    "https://rajeshkhandelwal.com",
    "https://www.rajeshkhandelwal.com",

    "https://rajeshkhandelwalofficial.com",
    "https://www.rajeshkhandelwalofficial.com",

    "https://drrajeshkhandelwalibc.com",
    "https://www.drrajeshkhandelwalibc.com",

    "https://drrajeshkhandelwalibcofficial.com",
    "https://www.drrajeshkhandelwalibcofficial.com",

    # Render
    "https://rajeshkhandelwal.onrender.com",
    "https://rajeshkhandelwalofficial.onrender.com",
    "https://drrajeshkhandelwalibc.onrender.com",
    "https://drrajeshkhandelwalibcofficial.onrender.com",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROUTERS
# ============================================================

# SUPREME API
app.include_router(
    supreme_router
)

# CENTRAL HUB API
app.include_router(
    hub_router
)

# REPOSITORIES API
app.include_router(
    repositories_router
)


# ============================================================
# FRONTEND
# ============================================================
#
# IMPORTANT:
#
# Frontend content is NOT copied from SUPREMESETUHUB.
#
# This repository only serves its own frontend/index.html
# if that file exists.
#
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

FRONTEND_DIR = (
    BASE_DIR
    / "frontend"
)

FRONTEND_INDEX = (
    FRONTEND_DIR
    / "index.html"
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def home():

    # If this repository has its own frontend,
    # serve it directly.

    if FRONTEND_INDEX.is_file():

        return FileResponse(
            FRONTEND_INDEX,
            media_type="text/html",
        )

    # Otherwise return API information.
    return {
        "success": True,
        "message": "Welcome to DR RAJESH KHANDELWAL IBC",
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
        "repository": "DRRAJESHKHANDELWALIBC",
        "central_hub": "SUPREMESETUHUB",
        "status": "active",
        "frontend": "not_found",
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health_check():

    return {
        "success": True,
        "status": "healthy",
        "repository": "DRRAJESHKHANDELWALIBC",
        "central_hub": "SUPREMESETUHUB",
    }


# ============================================================
# METADATA
# ============================================================

@app.get("/metadata")
def metadata():

    return get_backend_metadata()


# ============================================================
# API STATUS
# ============================================================

@app.get("/api/status")
def api_status():

    return {
        "success": True,
        "service": "DR RAJESH KHANDELWAL IBC",
        "repository": "DRRAJESHKHANDELWALIBC",
        "central_hub": "SUPREMESETUHUB",
        "status": "active",
        "api": "online",
    }


# ============================================================
# FRONTEND STATIC FILES
# ============================================================
#
# This allows:
#
# /style.css
# /script.js
# /images/...
#
# to be served from this repository's frontend folder.
#
# ============================================================

@app.get("/{filename:path}")
def frontend_files(filename: str):

    requested_file = (
        FRONTEND_DIR
        / filename
    )

    if requested_file.is_file():

        return FileResponse(
            requested_file
        )

    return {
        "success": False,
        "error": "NOT_FOUND",
        "message": "The requested resource does not exist",
        "path": filename,
    }
