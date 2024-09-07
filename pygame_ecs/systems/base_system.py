from pygame_ecs.components.base import Component
from pygame_ecs.entity import Entity

from pygame_ecs.managers.entity_manager import EntityManager


class System:
    """A base system that all Systems must inherit from."""

    # TODO: make the update and update_entities function names less confusing
    # ALSO: add another update option for systems that will get entities as generator objects etc.
    def __init__(self, required_component_types: list[type[Component]]) -> None:
        self.required_component_types = required_component_types
        self.entity_manager: EntityManager

    def update_entity(
        self,
        entity: Entity,
        # AAAAAAAAAAAAAAAAAAAAAAAA
        # this typehint is based on dict version
        # AAAAAAA
        entity_components: any,
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
