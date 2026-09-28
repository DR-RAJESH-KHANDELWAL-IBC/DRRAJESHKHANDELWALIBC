"""
👑 DR RAJESH KHANDELWAL IBC 👑

SUPREMESETUHUB connection API.
"""

from fastapi import APIRouter

from backend.hub_client import (
    get_hub_status,
    check_hub_connection,
)

router = APIRouter(
    prefix="/hub",
    tags=["SUPREMESETUHUB"],
)


@router.get("/status")
def hub_status():
    """Return Central Hub configuration status."""
    return {
        "success": True,
        "hub": get_hub_status(),
    }


@router.get("/connection")
async def hub_connection():
    """Check Central Hub API reachability."""
    return {
        "success": True,
        "connection": await check_hub_connection(),
    }
