"""
👑 DR RAJESH KHANDELWAL IBC 👑
Session request and response models.
"""

from typing import Optional

from pydantic import BaseModel


class SessionCreateRequest(BaseModel):
    user_id: str
    device_info: Optional[str] = None


class SessionInfo(BaseModel):
    session_id: str
    user_id: str
    status: str = "active"
    device_info: Optional[str] = None


class SessionResponse(BaseModel):
    success: bool
    message: str
    session: Optional[SessionInfo] = None
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
