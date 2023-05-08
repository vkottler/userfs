"""
Hooks for the 'config' project.
"""

# built-in
from pathlib import Path
from typing import Any, Dict

# internal
from userfs.config import ProjectSpecification


def pre_fetch(
    root: Path,
    project: ProjectSpecification,
    interaction_options: Dict[str, Any],
    cli_options: Dict[str, Any],
) -> None:
    """Example project interaction."""

    print(root)
    print(project)
    print(interaction_options)
    print(cli_options)


def post_fetch(
    root: Path,
    project: ProjectSpecification,
    interaction_options: Dict[str, Any],
    cli_options: Dict[str, Any],
) -> None:
    """Example project interaction."""

    print(root)
    print(project)
    print(interaction_options)
    print(cli_options)
