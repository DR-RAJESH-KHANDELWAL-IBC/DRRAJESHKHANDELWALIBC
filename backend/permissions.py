"""
👑 DR RAJESH KHANDELWAL IBC 👑
Permission helpers for Supreme, Admin, and Owner roles.
"""

from backend.constants import ROLE_SUPREME, ROLE_ADMIN, ROLE_OWNER


ROLE_PERMISSIONS = {
    ROLE_SUPREME: ["*"],
    ROLE_ADMIN: [
        "users.read",
        "users.manage",
        "sessions.read",
    ],
    ROLE_OWNER: [
        "business.read",
        "business.manage",
        "profile.read",
        "profile.update",
    ],
}


def get_role_permissions(role: str) -> list[str]:
    """Return permissions assigned to a role."""
    return ROLE_PERMISSIONS.get(role.upper(), [])


def has_permission(role: str, permission: str) -> bool:
    """Check whether a role has a specific permission."""
    permissions = get_role_permissions(role)

    return "*" in permissions or permission in permissions
