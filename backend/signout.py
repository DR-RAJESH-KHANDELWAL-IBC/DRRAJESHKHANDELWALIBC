"""
👑 DR RAJESH KHANDELWAL IBC 👑
SIGNOUT request and response models.
"""

from typing import Optional

from pydantic import BaseModel


class SignOutRequest(BaseModel):
    session_id: Optional[str] = None
    access_token: Optional[str] = None


class SignOutResponse(BaseModel):
    success: bool
    message: str
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
