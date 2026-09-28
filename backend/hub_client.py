"""
👑 DR RAJESH KHANDELWAL IBC 👑

SUPREMESETUHUB API client configuration.
"""

import os

import httpx


HUB_NAME = "SUPREMESETUHUB"

HUB_API_BASE_URL = os.getenv(
    "SUPREMESETUHUB_API_URL",
    "",
).rstrip("/")


def get_hub_status() -> dict:
    """Return the configured Central Hub connection status."""

    if not HUB_API_BASE_URL:
        return {
            "connected": False,
            "hub": HUB_NAME,
            "message": "Central Hub API URL is not configured",
        }

    return {
        "connected": False,
        "hub": HUB_NAME,
        "api_base_url": HUB_API_BASE_URL,
        "message": "API URL configured; connection not yet verified",
    }


async def check_hub_connection() -> dict:
    """Check whether the Central Hub API is reachable."""

    if not HUB_API_BASE_URL:
        return get_hub_status()

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{HUB_API_BASE_URL}/health"
            )
            response.raise_for_status()

        return {
            "connected": True,
            "hub": HUB_NAME,
            "message": "Central Hub is reachable",
        }

    except httpx.HTTPError:
        return {
            "connected": False,
            "hub": HUB_NAME,
            "message": "Central Hub connection failed",
        }
