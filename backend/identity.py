"""
👑 DR RAJESH KHANDELWAL IBC 👑
Supreme Admin Owner identity models.
"""

from typing import Optional

from pydantic import BaseModel


class IdentityInfo(BaseModel):
    identity_id: str
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
    supreme: bool = True
    admin: bool = True
    owner: bool = True
    status: str = "active"


class IdentityResponse(BaseModel):
    success: bool
    message: str
    identity: Optional[IdentityInfo] = None
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
