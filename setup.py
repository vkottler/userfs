# =====================================
# generator=datazen
# version=3.1.4
# hash=f993f366d875477ffb6517fa8dcc1e1d
# =====================================

"""
userfs - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from userfs_bootstrap.setup import setup  # type: ignore

# internal
from userfs import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughnkottler@gmail.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.10",
        "3.11",
        "3.12",
    ],
}
setup(
    pkg_info,
    author_info,
)
