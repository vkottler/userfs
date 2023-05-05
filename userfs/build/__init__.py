"""
A module for building project sources.
"""

# built-in
from pathlib import Path

# internal
from userfs.config import ProjectSpecification


def build(root: Path, project: ProjectSpecification) -> None:
    """Build an individual project."""

    print(root)
    print(project)
