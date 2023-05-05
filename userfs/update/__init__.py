"""
A module for updating project sources.
"""

# built-in
from pathlib import Path

# internal
from userfs.config import ProjectSpecification


def update(root: Path, project: ProjectSpecification) -> None:
    """Update an individual project."""

    print(root)
    print(project)
