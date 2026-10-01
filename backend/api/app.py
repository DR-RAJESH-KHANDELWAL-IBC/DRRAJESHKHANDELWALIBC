"""
👑 DR RAJESH KHANDELWAL IBC 👑

Main FastAPI application.

SUPREME + ADMIN + OWNER

Central Hub:
SUPREMESETUHUB

Architecture:
DRRAJESHKHANDELWALIBC
        ↓
SUPREMESETUHUB
        ↓
CENTRAL FRONTEND
        ↓
HTML + CSS + JS + IMAGES + ASSETS
"""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import urljoin

import requests

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (
    Response,
    JSONResponse,
)

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
# SUPREME CENTRAL API
# ============================================================

SUPREME_API_URL = (
    "https://supremesetuhub-3v4e.onrender.com"
).rstrip("/")


# ============================================================
# SUPREME CENTRAL FRONTEND
# ============================================================

SUPREME_FRONTEND_URL = (
    SUPREME_API_URL
    + "/api/v1/frontend/supreme"
)


# ============================================================
# SUPREME FRONTEND ASSET BASE
# ============================================================
#
# Central frontend:
#
# SUPREMESETUHUB
#     ↓
# frontend/supreme/
#     ├── index.html
#     ├── style.css
#     ├── script.js
#     └── assets/
#
# ============================================================

SUPREME_FRONTEND_BASE = (
    SUPREME_API_URL
    + "/api/v1/frontend/supreme/"
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

app.include_router(supreme_router)
app.include_router(hub_router)
app.include_router(repositories_router)


# ============================================================
# HTTP CLIENT HELPERS
# ============================================================

def fetch_supreme(
    url: str,
    timeout: int = 30,
) -> requests.Response:

    return requests.get(
        url,
        timeout=timeout,
        allow_redirects=True,
    )


# ============================================================
# ROOT HOME PAGE
# ============================================================
#
# IMPORTANT:
#
# This repository does NOT use its own local frontend.
#
# The live homepage comes from:
#
# SUPREMESETUHUB
#       ↓
# /api/v1/frontend/supreme
#
# ============================================================

@app.get("/")
def home():

    try:

        response = fetch_supreme(
            SUPREME_FRONTEND_URL,
            timeout=30,
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="text/html",
            headers={
                "Cache-Control": "no-cache",
            },
        )

    except requests.RequestException as exc:

        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "error": "SUPREME_FRONTEND_UNAVAILABLE",
                "message": str(exc),
                "central_hub": "SUPREMESETUHUB",
                "frontend_source": SUPREME_FRONTEND_URL,
            },
        )


# ============================================================
# SUPREME FRONTEND CSS
# ============================================================
#
# /style.css
#      ↓
# SUPREMESETUHUB/style.css
#
# ============================================================

@app.get("/style.css")
def supreme_style_css():

    css_url = (
        SUPREME_FRONTEND_BASE
        + "style.css"
    )

    try:

        response = fetch_supreme(
            css_url,
            timeout=30,
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="text/css",
            headers={
                "Cache-Control": "no-cache",
            },
        )

    except requests.RequestException as exc:

        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "error": "SUPREME_CSS_UNAVAILABLE",
                "message": str(exc),
            },
        )


# ============================================================
# SUPREME FRONTEND JAVASCRIPT
# ============================================================

@app.get("/script.js")
def supreme_script_js():

    js_url = (
        SUPREME_FRONTEND_BASE
        + "script.js"
    )

    try:

        response = fetch_supreme(
            js_url,
            timeout=30,
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="application/javascript",
            headers={
                "Cache-Control": "no-cache",
            },
        )

    except requests.RequestException as exc:

        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "error": "SUPREME_JS_UNAVAILABLE",
                "message": str(exc),
            },
        )


# ============================================================
# SUPREME FRONTEND ASSETS
# ============================================================
#
# Examples:
#
# /assets/logo.png
# /images/banner.jpg
# /icons/icon.svg
#
# Everything is requested from SUPREMESETUHUB.
#
# ============================================================

@app.get("/assets/{asset_path:path}")
@app.get("/images/{asset_path:path}")
@app.get("/icons/{asset_path:path}")
@app.get("/fonts/{asset_path:path}")
def supreme_assets(
    asset_path: str,
    request: Request,
):

    current_path = request.url.path.lstrip("/")

    asset_url = urljoin(
        SUPREME_FRONTEND_BASE,
        current_path,
    )

    try:

        response = fetch_supreme(
            asset_url,
            timeout=30,
        )

        content_type = response.headers.get(
            "Content-Type",
            "application/octet-stream",
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=content_type.split(";")[0],
            headers={
                "Cache-Control": "no-cache",
            },
        )

    except requests.RequestException as exc:

        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "error": "SUPREME_ASSET_UNAVAILABLE",
                "message": str(exc),
                "asset": current_path,
            },
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
        "frontend_source": SUPREME_FRONTEND_URL,
        "architecture": "SUPREME CENTRAL FRONTEND",
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
        "frontend": "central",
    }


# ============================================================
# SUPREME CONNECTION STATUS
# ============================================================

@app.get("/supreme/connection")
def supreme_connection():

    try:

        response = fetch_supreme(
            SUPREME_API_URL
            + "/health",
            timeout=15,
        )

        try:
            upstream = response.json()
        except ValueError:
            upstream = {
                "status_code": response.status_code,
                "response": response.text[:500],
            }

        return {
            "success": response.status_code == 200,
            "repository": "DRRAJESHKHANDELWALIBC",
            "connected_to": "SUPREMESETUHUB",
            "central_api": SUPREME_API_URL,
            "central_frontend": SUPREME_FRONTEND_URL,
            "upstream": upstream,
        }

    except requests.RequestException as exc:

        raise HTTPException(
            status_code=502,
            detail={
                "error": "SUPREME_CONNECTION_FAILED",
                "message": str(exc),
                "central_hub": "SUPREMESETUHUB",
            },
        )


# ============================================================
# FALLBACK FRONTEND ROUTES
# ============================================================
#
# This handles additional frontend files if required.
#
# Example:
#
# /favicon.ico
# /manifest.json
# /robots.txt
#
# ============================================================

@app.get(
    "/{filename:path}",
    include_in_schema=False,
)
def frontend_fallback(
    filename: str,
):

    # Never intercept API routes.
    if (
        filename.startswith("api/")
        or filename.startswith("supreme/")
        or filename == "health"
        or filename == "metadata"
    ):
        raise HTTPException(
            status_code=404,
            detail="NOT_FOUND",
        )

    requested_url = urljoin(
        SUPREME_FRONTEND_BASE,
        filename,
    )

    try:

        response = fetch_supreme(
            requested_url,
            timeout=30,
        )

        if response.status_code >= 400:

            raise HTTPException(
                status_code=response.status_code,
                detail="RESOURCE_NOT_FOUND",
            )

        content_type = response.headers.get(
            "Content-Type",
            "application/octet-stream",
        )

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=content_type.split(";")[0],
            headers={
                "Cache-Control": "no-cache",
            },
        )

    except requests.RequestException as exc:

        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "error": "SUPREME_RESOURCE_UNAVAILABLE",
                "message": str(exc),
                "resource": filename,
            },
        )


# ============================================================
# LOCAL RUN
# ============================================================

if __name__ == "__main__":

    import uvicorn

    port = int(
        os.getenv(
            "PORT",
            "10000",
        )
    )

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
    )
