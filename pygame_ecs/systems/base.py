from typing import TypeVar

from pygame_ecs.components.base import Component
from pygame_ecs.entity import Entity


CompType = TypeVar("CompType", bound=Component)


class System:
    def __init__(self, component_types: list[type[CompType]]) -> None:
        self.component_types = component_types

    def update_entity(
        self,
        entity: Entity,
        # What a shitty type hint, fuck this
        entity_components: dict[type[CompType], Component],
    ):
        """This function is called for every entity that has the required components if the required component size is bigger than 0.

        Entity_components is a dict with component types as dict and component subclass instances as values.
        """
        pass

    def update(self):
        """This function is called only once a frame if the required components is 0."""
        pass

    def __str__(self) -> str:
        return f"<{type(self).__name__}>"
