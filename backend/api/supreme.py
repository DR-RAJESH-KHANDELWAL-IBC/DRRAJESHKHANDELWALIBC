"""
👑 DR RAJESH KHANDELWAL IBC 👑
SUPREME, ADMIN, OWNER API.
"""

from fastapi import APIRouter

from backend.repository_config import get_repository_config
from backend.role_service import get_all_roles

router = APIRouter(
    prefix="/supreme",
    tags=["SUPREME ADMIN OWNER"],
)


@router.get("/status")
def get_supreme_status():
    return {
        "success": True,
        "message": "SUPREME system is active",
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
        "repository": "DRRAJESHKHANDELWALIBC",
        "central_hub": "SUPREMESETUHUB",
        "status": "active",
    }


@router.get("/profile")
def get_supreme_profile():
    return {
        "success": True,
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
        "roles": ["SUPREME", "ADMIN", "OWNER"],
        "repository": "DRRAJESHKHANDELWALIBC",
    }


@router.get("/repository")
def get_repository():
    return {
        "success": True,
        "repository": get_repository_config(),
    }


@router.get("/roles")
def get_roles():
    return {
        "success": True,
        "roles": [
            role.model_dump()
            for role in get_all_roles()
        ],
    }
