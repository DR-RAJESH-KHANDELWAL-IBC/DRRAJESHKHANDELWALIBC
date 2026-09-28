"""
👑 DR RAJESH KHANDELWAL IBC 👑

API for viewing the four registered repositories.
"""

from fastapi import APIRouter, HTTPException

from backend.repositories import (
    get_all_repositories,
    get_repository,
)

router = APIRouter(
    prefix="/repositories",
    tags=["REPOSITORIES"],
)


@router.get("/")
def list_repositories():
    """Return all registered repositories."""
    return {
        "success": True,
        "repositories": get_all_repositories(),
    }


@router.get("/{repository_name}")
def repository_details(repository_name: str):
    """Return details of a registered repository."""
    repository = get_repository(repository_name)

    if repository is None:
        raise HTTPException(
            status_code=404,
            detail="Repository not found",
        )

    return {
        "success": True,
        "repository": repository,
    }
