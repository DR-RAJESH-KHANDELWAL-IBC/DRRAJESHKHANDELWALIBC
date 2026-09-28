"""
👑 DR RAJESH KHANDELWAL IBC 👑
Email verification request and response models.
"""

from pydantic import BaseModel, EmailStr


class EmailVerificationRequest(BaseModel):
    email: EmailStr


class EmailVerificationConfirm(BaseModel):
    email: EmailStr
    verification_code: str


class EmailVerificationResponse(BaseModel):
    success: bool
    message: str
    verified: bool = False
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
