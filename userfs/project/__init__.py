"""
A module for interfacing with projects.
"""

# built-in
from enum import Enum, auto
from multiprocessing import Pool
from pathlib import Path
from typing import Iterable, NamedTuple

# internal
from userfs.build import build
from userfs.config import Config, Interact, ProjectSpecification
from userfs.deploy import deploy
from userfs.fetch import fetch
from userfs.update import update


class ProjectInteraction(Enum):
    """Kinds of project interactions."""

    FETCH = auto()
    UPDATE = auto()
    BUILD = auto()
    DEPLOY = auto()


INTERACTIONS = {
    ProjectInteraction.FETCH: fetch,
    ProjectInteraction.UPDATE: update,
    ProjectInteraction.BUILD: build,
    ProjectInteraction.DEPLOY: deploy,
}


class ProjectInteractionTask(NamedTuple):
    """
    A data structure containing all information necessary for interacting with
    a project.
    """

    kind: ProjectInteraction
    root: Path
    project: ProjectSpecification

    def interact(self, interaction: Interact) -> None:
        """Run a project-interaction method."""
        interaction(self.root, self.project)


def interact(task: ProjectInteractionTask) -> None:
    """Perform a project interaction."""
    task.interact(INTERACTIONS[task.kind])


def execute_interactions(
    interactions: Iterable[ProjectInteraction],
    projects: Iterable[str],
    config: Config,
) -> int:
    """Execute project interactions in parallel."""

    for interaction in interactions:
        with Pool() as pool:
            pool.map(
                interact,
                [
                    ProjectInteractionTask(
                        interaction,
                        config.directory,
                        config.projects[x],
                    )
                    for x in projects
                ],
            )
            pool.close()
            pool.join()

    return 0
