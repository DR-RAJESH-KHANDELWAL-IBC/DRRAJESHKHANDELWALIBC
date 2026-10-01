"""
👑 DR RAJESH KHANDELWAL IBC 👑

Main FastAPI application.
SUPREME + ADMIN + OWNER

Central Hub:
SUPREMESETUHUB
"""

from __future__ import annotations

from typing import Optional

import httpx

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

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
# SUPREMESETUHUB
# CENTRAL FRONTEND + API SOURCE
# ============================================================

SUPREMESETUHUB_URL = (
    "https://supremesetuhub-3v4e.onrender.com"
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

    # Current Render service
    "https://drrajeshkhandelwalibc-vbmq.onrender.com",
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
# SUPREME FRONTEND PROXY
# ============================================================

async def fetch_supreme_frontend(
    path: str = "",
):
    """
    Fetch frontend content directly from SUPREMESETUHUB.

    No HTML/CSS/JS is copied into this repository.
    SUPREMESETUHUB remains the central source.
    """

    clean_path = path.lstrip("/")

    if clean_path:
        target_url = (
            SUPREMESETUHUB_URL.rstrip("/")
            + "/"
            + clean_path
        )
    else:
        target_url = (
            SUPREMESETUHUB_URL.rstrip("/")
            + "/"
        )

    try:

        async with httpx.AsyncClient(
            follow_redirects=True,
            timeout=30.0,
        ) as client:

            response = await client.get(
                target_url
            )

        content_type = response.headers.get(
            "content-type",
            "text/html; charset=utf-8",
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=content_type.split(";")[0],
        )

    except httpx.RequestError as exc:

        raise HTTPException(
            status_code=502,
            detail={
                "error": "SUPREMESETUHUB_UNAVAILABLE",
                "message": str(exc),
                "upstream": target_url,
            },
        )


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/")
async def home():

    return await fetch_supreme_frontend()


# ============================================================
# SUPREME FRONTEND ASSETS
# ============================================================
#
# Examples:
#
# /style.css
# /script.js
# /images/logo.png
# /assets/...
#
# These are requested from SUPREMESETUHUB.
#
# Nothing is copied locally.
# ============================================================

@app.get("/style.css")
async def supreme_style_css():

    return await fetch_supreme_frontend(
        "style.css"
    )


@app.get("/script.js")
async def supreme_script_js():

    return await fetch_supreme_frontend(
        "script.js"
    )


@app.get("/images/{path:path}")
async def supreme_images(path: str):

    return await fetch_supreme_frontend(
        f"images/{path}"
    )


@app.get("/assets/{path:path}")
async def supreme_assets(path: str):

    return await fetch_supreme_frontend(
        f"assets/{path}"
    )


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
        "frontend_source": SUPREMESETUHUB_URL,
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
        "frontend": "connected",
    }


# ============================================================
# SUPREME FRONTEND FALLBACK
# ============================================================
#
# Any additional frontend file requested by the browser
# will be fetched from SUPREMESETUHUB.
#
# API routes above remain protected because FastAPI checks
# the more specific routes first.
# ============================================================

@app.get("/{frontend_path:path}")
async def frontend_proxy(
    frontend_path: str,
):

    # Do not proxy API/system endpoints as frontend assets.

    protected_paths = (
        "api/",
        "health",
        "metadata",
        "docs",
        "redoc",
        "openapi.json",
    )

    if frontend_path.startswith(
        protected_paths
    ):

        raise HTTPException(
            status_code=404,
            detail="Endpoint not found",
        )

    return await fetch_supreme_frontend(
        frontend_path
    )
