"""
👑 DR RAJESH KHANDELWAL IBC 👑
Backend metadata helper.
"""

from backend.constants import BACKEND_NAME, BACKEND_VERSION, BACKEND_STATUS


def get_backend_metadata() -> dict:
    return {
        "name": BACKEND_NAME,
        "version": BACKEND_VERSION,
        "status": BACKEND_STATUS,
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
    }
