"""
Test the 'commands.build' module.
"""

# internal
from tests.resources import resource

# module under test
from userfs import PKG_NAME
from userfs.entry import main as userfs_main


def test_build_command_basic():
    """Test the 'build' command."""

    assert userfs_main([PKG_NAME, "build"]) == 0
    assert (
        userfs_main([PKG_NAME, "build", "-c", str(resource(".")), "runtimepy"])
        == 0
    )
    assert (
        userfs_main(
            [PKG_NAME, "build", "-c", str(resource(".")), "-d", "runtimepy"]
        )
        == 0
    )
