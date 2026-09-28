"""
👑 DR RAJESH KHANDELWAL IBC 👑
Repository registry for SUPREMESETUHUB.
"""

from backend.repository_config import (
    REPOSITORY_NAME,
    DISPLAY_NAME,
    CENTRAL_HUB_NAME,
)


REPOSITORY_REGISTRY = {
    REPOSITORY_NAME: {
        "repository_name": REPOSITORY_NAME,
        "display_name": DISPLAY_NAME,
        "central_hub": CENTRAL_HUB_NAME,
        "roles": ["SUPREME", "ADMIN", "OWNER"],
        "status": "active",
    }
}


def get_registered_repository(repository_name: str) -> dict | None:
    """Return repository details by name."""
    return REPOSITORY_REGISTRY.get(repository_name)


def get_all_registered_repositories() -> list[dict]:
    """Return all registered repositories."""
    return list(REPOSITORY_REGISTRY.values())
