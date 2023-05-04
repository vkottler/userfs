"""
An entry-point for the 'fetch' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from userfs.config import load_config


def fetch_cmd(args: _Namespace) -> int:
    """Execute the fetch command."""

    result = 0

    config = load_config(root=args.config)
    print(config)

    return result


def add_fetch_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add fetch-command arguments to its parser."""

    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        help="an optional path to the configuration directory",
    )

    return fetch_cmd
