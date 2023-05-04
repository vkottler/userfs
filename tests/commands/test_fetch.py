"""
Test the 'commands.fetch' module.
"""

# internal
from tests.resources import resource

# module under test
from userfs import PKG_NAME
from userfs.entry import main as userfs_main


def test_fetch_command_basic():
    """Test the 'fetch' command against the 'empty' scenario."""

    assert userfs_main([PKG_NAME, "fetch"]) == 0
    assert userfs_main([PKG_NAME, "fetch", "-c", str(resource("."))]) == 0
