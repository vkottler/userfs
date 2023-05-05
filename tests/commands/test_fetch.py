"""
Test the 'commands.fetch' module.
"""

# internal
from shutil import rmtree

# module under test
from tests.resources import resource
from userfs import PKG_NAME
from userfs.entry import main as userfs_main


def test_fetch_command_basic():
    """Test the 'fetch' command."""

    # Remove the directory tree that we're fetching assets to.
    rmtree(resource("..", "src"))

    assert userfs_main([PKG_NAME, "fetch"]) == 0
    assert userfs_main([PKG_NAME, "fetch", "-c", str(resource("."))]) == 0
    assert (
        userfs_main([PKG_NAME, "fetch", "-c", str(resource(".")), "-a", "-u"])
        == 0
    )
