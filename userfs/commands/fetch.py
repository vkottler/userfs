"""
An entry-point for the 'fetch' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from userfs.commands.common import add_common, get_projects
from userfs.config import load_config
from userfs.project import ProjectInteraction, execute_interactions


def fetch_cmd(args: _Namespace) -> int:
    """Execute the fetch command."""

    interactions = [ProjectInteraction.FETCH]
    if args.update:
        interactions.append(ProjectInteraction.UPDATE)

    config = load_config(root=args.config)
    return execute_interactions(
        interactions, get_projects(args, config), config
    )


def add_fetch_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add fetch-command arguments to its parser."""

    add_common(parser)
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="interact with all configured projects",
    )
    parser.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="whether or not to also attempt to update project sources",
    )
    parser.add_argument(
        "projects", nargs="*", help="specific projects to fetch"
    )

    return fetch_cmd
