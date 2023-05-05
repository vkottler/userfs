"""
An entry-point for the 'fetch' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from multiprocessing import Pool

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from userfs.commands.common import add_common
from userfs.config import ProjectSpecification, load_config


def fetch_project(project: ProjectSpecification) -> None:
    """Fetch an individual project."""

    print(project.url)


def fetch_cmd(args: _Namespace) -> int:
    """Execute the fetch command."""

    config = load_config(root=args.config)

    if args.all:
        names = set(config.projects.keys())
    else:
        names = set(args.projects)

    # Get project references.
    with Pool() as pool:
        pool.map(fetch_project, [config.projects[x] for x in names])
        pool.close()
        pool.join()

    return 0


def add_fetch_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add fetch-command arguments to its parser."""

    add_common(parser)
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="fetch all configured projects",
    )
    parser.add_argument(
        "projects", nargs="*", help="specific projects to fetch"
    )

    return fetch_cmd
