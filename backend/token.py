"""
👑 DR RAJESH KHANDELWAL IBC 👑
Authentication token request and response models.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TokenRequest(BaseModel):
    user_id: str
    session_id: Optional[str] = None


class TokenInfo(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_at: Optional[datetime] = None


class TokenResponse(BaseModel):
    success: bool
    message: str
    token: Optional[TokenInfo] = None
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
