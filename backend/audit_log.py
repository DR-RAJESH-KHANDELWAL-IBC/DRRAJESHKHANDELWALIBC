"""
👑 DR RAJESH KHANDELWAL IBC 👑
Audit records for Supreme, Admin, and Owner activities.
"""

from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, Field


class AuditLogEntry(BaseModel):
    audit_id: str
    actor_id: str
    actor_role: str
    action: str
    resource: Optional[str] = None
    status: str = "success"
    details: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"


class AuditLogResponse(BaseModel):
    success: bool
    message: str
    entries: list[AuditLogEntry] = Field(default_factory=list)
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC 👑"
