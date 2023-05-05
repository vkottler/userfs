"""
Common argument-parsing utilities for package commands.
"""
# built-in
from argparse import ArgumentParser as _ArgumentParser
from pathlib import Path as _Path


def add_common(parser: _ArgumentParser) -> None:
    """Add common command options."""

    parser.add_argument(
        "-c",
        "--config",
        type=_Path,
        help="an optional path to the configuration directory",
    )
