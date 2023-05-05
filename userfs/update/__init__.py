"""
A module for updating project sources.
"""

# built-in
from pathlib import Path
from typing import Any, Dict

# third-party
from git import Repo  # type: ignore

# internal
from userfs.config import ProjectSpecification


def update(
    root: Path, project: ProjectSpecification, options: Dict[str, Any]
) -> None:
    """Update an individual project."""

    repo = Repo(project.location(root=root))

    remote_name = options.get("remote", "origin")
    if remote_name in repo.remotes:
        remote = repo.remotes[remote_name]
        remote.pull()
