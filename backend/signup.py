"""
👑 DR RAJESH KHANDELWAL IBC 👑
SIGNUP request and response models.
"""

from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class SignUpRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=150)
    email: EmailStr
    password: str = Field(..., min_length=8)


class SignUpResponse(BaseModel):
    success: bool
    message: str
    user_id: Optional[str] = None
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
