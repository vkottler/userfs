# =====================================
# generator=datazen
# version=3.1.2
# hash=3a5f184e2c33991db6f30683b9fe86cf
# =====================================

"""
A module aggregating package commands.
"""

# built-in
from typing import List as _List
from typing import Tuple as _Tuple

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from userfs.commands.fetch import add_fetch_cmd
from userfs.commands.build import add_build_cmd


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "fetch",
            "attempt to obtain some software from the internet",
            add_fetch_cmd,
        ),
        (
            "build",
            "attempt to build a software project from its sources",
            add_build_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
