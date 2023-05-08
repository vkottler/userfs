"""
A module implementing interfaces to interact with external scripts and modules.
"""

# built-in
from typing import Callable, Optional

# internal
from userfs.config import Config, Interact, ProjectInteraction

HookLoader = Callable[[str, ProjectInteraction, Config], Optional[Interact]]


def get_hook(
    prefix: str, project: str, interaction: ProjectInteraction, config: Config
) -> Optional[Interact]:
    """Attempt to load a certain kind of project hook."""

    hook_name = f"{prefix}_{interaction.value}"
    print(hook_name)

    result = None

    print(project)
    print(config)

    return result
