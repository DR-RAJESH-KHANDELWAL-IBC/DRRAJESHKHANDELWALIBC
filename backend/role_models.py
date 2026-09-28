"""
👑 DR RAJESH KHANDELWAL IBC 👑
SUPREME, ADMIN, OWNER role models.
"""

from typing import Optional

from pydantic import BaseModel


class RoleInfo(BaseModel):
    role_id: str
    role_name: str
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
    status: str = "active"


class RoleAssignment(BaseModel):
    identity_id: str
    role_name: str
    repository_name: str = "DRRAJESHKHANDELWALIBC"
    status: str = "active"


class RoleResponse(BaseModel):
    success: bool
    message: str
    role: Optional[RoleInfo] = None
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
