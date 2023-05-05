"""
A module for working with test data.
"""

# built-in
from contextlib import contextmanager
from pathlib import Path
from shutil import rmtree
from typing import Iterator


@contextmanager
def src_cleaned() -> Iterator[None]:
    """Ensure that checked-out sources are cleaned up as a context."""

    path = resource("..", "src")
    rmtree(path, ignore_errors=True)
    path.mkdir()
    try:
        yield
    finally:
        rmtree(path, ignore_errors=True)


def resource(resource_name: str, *parts: str, valid: bool = True) -> Path:
    """Locate the path to a test resource."""

    return Path(__file__).parent.joinpath(
        "data", "valid" if valid else "invalid", resource_name, *parts
    )
