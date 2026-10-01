from __future__ import annotations

import os
from urllib.parse import quote

import requests

from flask import (
    Flask,
    jsonify,
    request,
    Response,
)


# ============================================================
# APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# SUPREME CENTRAL API
# ============================================================

SUPREME_API_URL = (
    "https://supremesetuhub-3v4e.onrender.com"
)


# ============================================================
# SUPREME CENTRAL FRONTEND
# ============================================================
#
# FRONTEND IS NOT DUPLICATED IN THIS REPOSITORY.
#
# This repository receives the live frontend from:
#
# SUPREMESETUHUB
#        ↓
# /api/v1/frontend/supreme
#
# ============================================================

SUPREME_FRONTEND_URL = (
    SUPREME_API_URL.rstrip("/")
    + "/api/v1/frontend/supreme"
)


# ============================================================
# CORS
# ============================================================

@app.after_request
def after_request(response):

    response.headers["Access-Control-Allow-Origin"] = "*"

    response.headers["Access-Control-Allow-Headers"] = (
        "Content-Type,Authorization"
    )

    response.headers["Access-Control-Allow-Methods"] = (
        "GET,PUT,POST,DELETE,OPTIONS"
    )

    return response


# ============================================================
# HOME PAGE
# ============================================================
#
# IMPORTANT:
#
# The home page is fetched LIVE from SUPREMESETUHUB.
#
# No local index.html is required.
# No HTML duplication.
# No CSS duplication.
#
# ============================================================

@app.get("/")
def root():

    try:

        response = requests.get(
            SUPREME_FRONTEND_URL,
            timeout=30,
            allow_redirects=True,
        )

        content_type = response.headers.get(
            "Content-Type",
            "text/html; charset=utf-8",
        )

        return Response(
            response.content,
            status=response.status_code,
            content_type=content_type,
        )

    except requests.RequestException as exc:

        return jsonify(
            {
                "success": False,
                "error": "SUPREME_FRONTEND_UNAVAILABLE",
                "message": str(exc),
                "service": "DRRAJESHKHANDELWAL",
                "supreme_api": SUPREME_API_URL,
                "supreme_frontend": SUPREME_FRONTEND_URL,
            }
        ), 502


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    return jsonify(
        {
            "success": True,
            "service": "RAJESHKHANDELWAL",
            "status": "healthy",
            "frontend_source": SUPREME_FRONTEND_URL,
            "architecture": "SUPREME CENTRAL FRONTEND",
            "connected_to": "SUPREMESETUHUB",
        }
    ), 200


# ============================================================
# SUPREME BRIDGE
# ============================================================

def call_supreme(endpoint: str):

    url = (
        SUPREME_API_URL.rstrip("/")
        + endpoint
    )

    try:

        response = requests.get(
            url,
            timeout=20,
        )

        try:

            payload = response.json()

        except ValueError:

            payload = {
                "error": (
                    "SUPREME returned "
                    "a non-JSON response"
                ),
                "status_code": response.status_code,
                "text": response.text[:1000],
            }

        return (
            response.status_code,
            payload,
        )

    except requests.RequestException as exc:

        return (
            500,
            {
                "error": str(exc),
                "upstream": SUPREME_API_URL,
            },
        )


# ============================================================
# SUPREME STATUS
# ============================================================

@app.get("/supreme/bridge/status")
def bridge_status():

    status_code, payload = call_supreme(
        "/supreme/status"
    )

    return jsonify(
        {
            "service": "RAJESHKHANDELWAL",
            "status": (
                "healthy"
                if status_code == 200
                else "bridge_error"
            ),
            "upstream": payload,
        }
    ), status_code


# ============================================================
# SUPREME PROFILE
# ============================================================

@app.get("/supreme/bridge/profile")
def bridge_profile():

    status_code, payload = call_supreme(
        "/supreme/profile"
    )

    return jsonify(
        {
            "service": "RAJESHKHANDELWAL",
            "status": (
                "healthy"
                if status_code == 200
                else "bridge_error"
            ),
            "profile": payload,
        }
    ), status_code


# ============================================================
# SUPREME SEARCH
# ============================================================

@app.get("/supreme/bridge/search")
def bridge_search():

    query = request.args.get(
        "q",
        "",
    ).strip()

    if not query:

        return jsonify(
            {
                "success": False,
                "error": "Missing q parameter",
            }
        ), 400

    encoded_query = quote(
        query,
        safe="",
    )

    status_code, payload = call_supreme(
        "/supreme/search?q="
        + encoded_query
    )

    return jsonify(
        {
            "service": "RAJESHKHANDELWAL",
            "status": (
                "healthy"
                if status_code == 200
                else "bridge_error"
            ),
            "results": payload,
        }
    ), status_code


# ============================================================
# CONNECTION STATUS
# ============================================================

@app.get("/supreme/connection")
def supreme_connection():

    return jsonify(
        {
            "success": True,
            "connected_to": "SUPREMESETUHUB",
            "identity": "👑 DR RAJESH KHANDELWAL IBC 👑",
            "message": (
                "👑 DR RAJESH KHANDELWAL IBC 👑 "
                "- Supreme Identity Profile 👑"
            ),
            "status": "ACTIVE",
            "frontend": SUPREME_FRONTEND_URL,
        }
    ), 200


# ============================================================
# 404 ERROR
# ============================================================

@app.errorhandler(404)
def not_found(error):

    return jsonify(
        {
            "success": False,
            "error": "NOT_FOUND",
            "message": (
                "The requested endpoint "
                "does not exist"
            ),
        }
    ), 404


# ============================================================
# 500 ERROR
# ============================================================

@app.errorhandler(500)
def server_error(error):

    return jsonify(
        {
            "success": False,
            "error": "SERVER_ERROR",
            "message": "Internal server error",
        }
    ), 500


# ============================================================
# LOCAL RUN
# ============================================================

if __name__ == "__main__":

    port = int(
        os.getenv(
            "PORT",
            "10000",
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
    )
