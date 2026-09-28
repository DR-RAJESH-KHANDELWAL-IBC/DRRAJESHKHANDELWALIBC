"""
👑 DR RAJESH KHANDELWAL IBC 👑
SUPREME, ADMIN, OWNER role service.
"""

from backend.constants import ROLE_SUPREME, ROLE_ADMIN, ROLE_OWNER
from backend.role_models import RoleInfo, RoleAssignment


REPOSITORY_NAME = "DRRAJESHKHANDELWALIBC"

ROLE_DEFINITIONS = {
    ROLE_SUPREME: {
        "role_id": "ROLE_SUPREME",
        "role_name": ROLE_SUPREME,
    },
    ROLE_ADMIN: {
        "role_id": "ROLE_ADMIN",
        "role_name": ROLE_ADMIN,
    },
    ROLE_OWNER: {
        "role_id": "ROLE_OWNER",
        "role_name": ROLE_OWNER,
    },
}


def get_role(role_name: str) -> RoleInfo | None:
    """Return role details by role name."""
    role = ROLE_DEFINITIONS.get(role_name.upper())

    if role is None:
        return None

    return RoleInfo(**role)


def get_all_roles() -> list[RoleInfo]:
    """Return all available roles."""
    return [
        RoleInfo(**role)
        for role in ROLE_DEFINITIONS.values()
    ]


def create_role_assignment(
    identity_id: str,
    role_name: str,
) -> RoleAssignment:
    """Create a role assignment for the repository."""
    normalized_role = role_name.upper()

    if normalized_role not in ROLE_DEFINITIONS:
        raise ValueError("Invalid role name")

    return RoleAssignment(
        identity_id=identity_id,
        role_name=normalized_role,
        repository_name=REPOSITORY_NAME,
    )
