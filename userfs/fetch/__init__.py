"""
A module for fetching projects.
"""

# built-in
from pathlib import Path

# internal
from userfs.config import ProjectSpecification, SourceKind


def fetch(root: Path, project: ProjectSpecification) -> None:
    """Fetch an individual project."""

    print(root)

    if project.source.kind is SourceKind.GIT:
        print("TODO")

    print(project.url)
