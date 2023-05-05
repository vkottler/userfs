"""
A module for building project sources.
"""

from __future__ import annotations

# built-in
from pathlib import Path
from typing import Dict, Any, List
import subprocess

# third-party
from vcorelib.logging import LoggerType

# internal
from userfs.config import ProjectSpecification


def run_process(
    logger: LoggerType, args: List[str]
) -> subprocess.CompletedProcess[str]:
    """Run a command-line process."""

    logger.info("Starting %s.", args)
    result = subprocess.run(args, check=False, text=True)
    logger.info("Exited %d.", result.returncode)
    return result


def build(_: Path, project: ProjectSpecification, __: Dict[str, Any]) -> None:
    """Build an individual project."""

    if project.attributes.get("mk"):
        if project.attributes.get("python"):
            run_process(
                project.logger, ["mk", "-C", str(project.location), "dz-sync"]
            )
            run_process(
                project.logger,
                ["mk", "-C", str(project.location), "python-build"],
            )
