"""
👑 DR RAJESH KHANDELWAL IBC 👑
Repository configuration for the Supreme Admin Owner system.
"""

REPOSITORY_NAME = "DRRAJESHKHANDELWALIBC"

DISPLAY_NAME = "👑 DR RAJESH KHANDELWAL IBC 👑"

CENTRAL_HUB_NAME = "SUPREMESETUHUB"

REPOSITORY_STATUS = "active"

SUPREME_ADMIN_OWNER = {
    "display_name": DISPLAY_NAME,
    "supreme": True,
    "admin": True,
    "owner": True,
}

def get_repository_config() -> dict:
    return {
        "repository_name": REPOSITORY_NAME,
        "display_name": DISPLAY_NAME,
        "central_hub": CENTRAL_HUB_NAME,
        "status": REPOSITORY_STATUS,
        "identity": SUPREME_ADMIN_OWNER.copy(),
    }
