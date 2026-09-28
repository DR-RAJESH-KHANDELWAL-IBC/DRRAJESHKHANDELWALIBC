"""
👑 DR RAJESH KHANDELWAL IBC 👑
Password reset request and confirmation models.
"""

from pydantic import BaseModel, EmailStr, Field


class PasswordResetRequest(BaseModel):
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    email: EmailStr
    reset_token: str
    new_password: str = Field(..., min_length=8)


class PasswordResetResponse(BaseModel):
    success: bool
    message: str
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
