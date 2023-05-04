"""
A module implementing a configuration interface for the package.
"""

# built-in
from os.path import expandvars
from pathlib import Path

# third-party
from rcmpy.xdg import user_config
from vcorelib.dict import merge
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec
from vcorelib.io import ARBITER as _ARBITER
from vcorelib.io.types import JsonObject as _JsonObject
from vcorelib.paths import Pathlike, find_file, normalize

# internal
from userfs import PKG_NAME
from userfs.schemas import UserfsDictCodec as _UserfsDictCodec


class Config(_UserfsDictCodec, _BasicDictCodec):
    """The top-level configuration object for the package."""

    def init(self, data: _JsonObject) -> None:
        """Initialize this instance."""
        self.data = data

        # Directory where all actions should be carried out.
        self.directory: Path = Path(
            expandvars(str(data["directory"]))
        ).expanduser()


def load_config(root: Pathlike = None, name: str = "config.yaml") -> Config:
    """
    Load this package's configuration as a managed context. If changed at
    runtime, changes will be written back to disk.
    """

    if root is None:
        root = user_config(PKG_NAME)

    src_config = find_file("config.yaml", package=PKG_NAME)
    assert src_config is not None

    return Config.create(
        merge(
            _ARBITER.decode(
                src_config, includes_key="includes", require_success=True
            ).data,
            _ARBITER.decode(
                normalize(root, name), includes_key="includes"
            ).data,
        )
    )
