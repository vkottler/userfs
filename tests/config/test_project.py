"""
Test the 'config.project' module.
"""

# internal
from tests.resources import resource

# module under test
from userfs.config import load_config


def test_project_specification_basic():
    """Test basic interactions with a project specification."""

    config = load_config(resource("."))

    source = config.sources["github"]
    source.protocol = "ssh"

    assert (
        config.projects["config"].url
        == "ssh://git@github.com/vkottler/config.git"
    )

    source.port = 22

    assert (
        config.projects["config"].url
        == "ssh://git@github.com:22/vkottler/config.git"
    )
