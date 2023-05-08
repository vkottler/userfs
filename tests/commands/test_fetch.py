"""
Test the 'commands.fetch' module.
"""

# internal
from tests.resources import resource, src_cleaned

# module under test
from userfs import PKG_NAME
from userfs.entry import main as userfs_main


def test_fetch_command_basic():
    """Test the 'fetch' command."""

    with src_cleaned():
        assert userfs_main([PKG_NAME, "fetch"]) == 0
        assert userfs_main([PKG_NAME, "fetch", "-c", str(resource("."))]) == 0
        assert (
            userfs_main(
                [
                    PKG_NAME,
                    "fetch",
                    "-c",
                    str(resource(".")),
                    "-a",
                    "-u",
                    "a=1",
                    "b=2",
                    "c=3",
                ]
            )
            == 0
        )

        # Coverage.
        assert userfs_main([PKG_NAME, "custom", "-c", str(resource("."))]) == 0
