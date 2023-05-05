"""
A module for deploying project sources.
"""

# built-in
from pathlib import Path

# internal
from userfs.config import ProjectSpecification


def deploy(root: Path, project: ProjectSpecification) -> None:
    """Deploy an individual project."""

    print(root)
    print(project)
