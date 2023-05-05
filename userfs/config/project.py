"""
A module implementing a data structure describing projects.
"""

# built-in
from dataclasses import dataclass
from typing import Any, Dict, cast

# third-party
from vcorelib.io import JsonObject

# internal
from userfs.config.source import SourceSpecification


@dataclass
class ProjectSpecification:
    """Information describing a software project and how to obtain it."""

    source: SourceSpecification
    path: str
    repository: str
    options: Dict[str, Any]

    @property
    def url(self) -> str:
        """Get a URL to this project's source."""

        source = self.source
        proto = source.protocol
        result = f"{source.protocol}://"

        if proto == "ssh":
            result += source.user + "@"

        result += source.host

        if source.port is not None:
            result += ":" + str(source.port)

        return result + "/" + self.path + "/" + self.repository + source.suffix

    @staticmethod
    def from_json(
        data: JsonObject, source: SourceSpecification, key: str
    ) -> "ProjectSpecification":
        """Create a project specification from JSON data."""

        return ProjectSpecification(
            source,
            cast(str, data["path"]),
            cast(str, data.get("repository", key)),
            cast(Dict[str, Any], data.get("options", {})),
        )
