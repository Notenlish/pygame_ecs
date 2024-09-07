import typing
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame_ecs.managers.component_manager import ComponentManager

from pygame_ecs.backends.base import BaseBackend
from pygame_ecs.components.base import BaseComponent
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import EntityDoesNotHaveComponent

# TODO: fix the component type hints for functions


class ListBackend(BaseBackend):
    """A backend that uses Lists with id's to store components."""

    __slots__ = ("component_types", "components")

    def __init__(self, component_manager: "ComponentManager") -> None:
        super().__init__(component_manager)
        # TODO: convert to list
        self.component_types: list[BaseComponent] = []
        self.components = {}
        # TODO: actually write good type hints

    def _add_component_type(self, component_type: BaseComponent):
        """Adds a component type. You generally don't need to manually call this if your components are subclasses of BaseComponent"""
        self.component_types.append(component_type)
        self.components[component_type._uid] = {}

    def _init_component(self, component_type: BaseComponent):
        self._add_component_type(component_type)

    def add_component(self, entity: Entity, component: BaseComponent):
        """Adds a component to an entity.

        Args:
            entity (Entity): Entity instance
            component (BaseComponent): Component that subclasses BaseComponent
        """
        self.components[component._uid][entity] = component

    def remove_component(self, entity: Entity, component_type: BaseComponent):
        try:
            del self.components[component_type._uid][entity]
        except KeyError:
            raise EntityDoesNotHaveComponent()

    def get_entity_components(
        self, entity: Entity, component_types: list[BaseComponent]
    ):
        # most time is spent here
        # big brain time: What if I did components[entity][comp_type]
        # instead of components[comp_type][entity]
        # LOL
        # wait I also have to change it to use a list so this is kinda useless.
        try:
            components = []
            for component_type in component_types:
                component = self.components[component_type._uid][entity]
                components.append(component)
            return components
        except KeyError:
            raise EntityDoesNotHaveComponent()

    def get_component_types(self):
        for component_type in self.component_types:
            yield component_type
