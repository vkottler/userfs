# =====================================
# generator=datazen
# version=3.1.2
# hash=941aadeb24c126b72884017b219348b1
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


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "fetch",
            "attempt to obtain some software from the internet",
            add_fetch_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
