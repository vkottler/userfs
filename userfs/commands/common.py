"""
Common argument-parsing utilities for package commands.
"""
# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path as _Path
from typing import Set

# internal
from userfs.config import Config


def add_common(parser: _ArgumentParser) -> None:
    """Add common command options."""

    parser.add_argument(
        "-c",
        "--config",
        type=_Path,
        help="an optional path to the configuration directory",
    )


def get_projects(args: _Namespace, config: Config) -> Set[str]:
    """Get a set of projects based on command-line arguments."""

    if args.all:
        names = set(config.projects.keys())
    else:
        names = set(args.projects)

    return names
