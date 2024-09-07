import typing

from pygame_ecs.components.base_component import Component
from pygame_ecs.entity import Entity
from pygame_ecs.managers.component_manager import ComponentInstanceType
from pygame_ecs.managers.entity_manager import EntityManager


class System:
    # typing.Type specifies that it will take subclasses of this class
    def __init__(self, required_component_types: list[typing.Type[Component]]) -> None:
        self.required_component_types = required_component_types
        self.entity_manager: EntityManager

    def update_entity(
        self,
        entity: Entity,
        entity_components: dict[typing.Type[Component], ComponentInstanceType],
    ):
        """This function is called for every entity that has the required components if the required component size is bigger than 0.

        Args:
            entity (Entity): Entity instance

            entity_components (dict[typing.Type[BaseComponent], ComponentInstanceType]): Components of the entity
        """
        pass

    def update(self):
        """This function is called only once a frame if the required components is 0."""
        pass

    def __str__(self) -> str:
        return f"<{type(self).__name__}>"
