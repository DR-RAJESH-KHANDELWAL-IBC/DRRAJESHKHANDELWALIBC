"""
👑 DR RAJESH KHANDELWAL IBC 👑

Registry of all four repositories and their API URLs.
"""

import os


REPOSITORIES = {
    "RAJESHKHANDELWAL": {
        "name": "RAJESHKHANDELWAL",
        "url": os.getenv("RAJESHKHANDELWAL_URL", ""),
        "www_url": os.getenv("RAJESHKHANDELWAL_WWW_URL", ""),
        "api_url": os.getenv("RAJESHKHANDELWAL_API_URL", ""),
    },
    "DRRAJESHKHANDELWALIBC": {
        "name": "DRRAJESHKHANDELWALIBC",
        "url": os.getenv("DRRAJESHKHANDELWALIBC_URL", ""),
        "www_url": os.getenv("DRRAJESHKHANDELWALIBC_WWW_URL", ""),
        "api_url": os.getenv("DRRAJESHKHANDELWALIBC_API_URL", ""),
    },
    "RAJESHKHANDELWALOFFICIAL": {
        "name": "RAJESHKHANDELWALOFFICIAL",
        "url": os.getenv("RAJESHKHANDELWALOFFICIAL_URL", ""),
        "www_url": os.getenv("RAJESHKHANDELWALOFFICIAL_WWW_URL", ""),
        "api_url": os.getenv("RAJESHKHANDELWALOFFICIAL_API_URL", ""),
    },
    "DRRAJESHKHANDELWALIBCOFFICIAL": {
        "name": "DRRAJESHKHANDELWALIBCOFFICIAL",
        "url": os.getenv("DRRAJESHKHANDELWALIBCOFFICIAL_URL", ""),
        "www_url": os.getenv("DRRAJESHKHANDELWALIBCOFFICIAL_WWW_URL", ""),
        "api_url": os.getenv("DRRAJESHKHANDELWALIBCOFFICIAL_API_URL", ""),
    },
}


def get_all_repositories() -> list[dict]:
    """Return all registered repositories."""
    return list(REPOSITORIES.values())


def get_repository(repository_name: str) -> dict | None:
    """Return repository details by name."""
    return REPOSITORIES.get(repository_name.upper())
