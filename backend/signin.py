"""
👑 DR RAJESH KHANDELWAL IBC 👑
SIGNIN request and response models.
"""

from typing import Optional

from pydantic import BaseModel, EmailStr


class SignInRequest(BaseModel):
    email: EmailStr
    password: str


class SignInResponse(BaseModel):
    success: bool
    message: str
    access_token: Optional[str] = None
    token_type: str = "bearer"
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
