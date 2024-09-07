import typing
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame_ecs.managers.component_manager import ComponentManager

from pygame_ecs.backends.base import BaseBackend
from pygame_ecs.components.base import Component
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import EntityDoesNotHaveComponent

# TODO: fix the component type hints for functions


class ListBackend(BaseBackend):
    """This is the default backend used by pygame_ecs. A backend that uses Lists with id's to store components."""

    def __init__(self, component_manager: "ComponentManager") -> None:
        super().__init__(component_manager)
        # TODO: actually write good type hints
        # TODO: convert to list
        # cant believe I just renamed it to ListBackend then refused to actually make it list based.
        self.component_types: list[Component] = []
        self.components: list[
            list[type[Component]]
        ] = []  # [entity] -> gives all components of that entity
        self.entity_len = 0

    def _add_component_type(self, component_type: type[Component]):
        """Adds a component type. You generally don't need to manually call this if your components are subclasses of BaseComponent"""
        self.component_types.append(component_type)

    def _init_component(self, component_type: type[Component]):
        self._add_component_type(component_type)

    def add_component(self, entity: Entity, component: type[Component]):
        """Adds a component to an entity.

        Args:
            entity (Entity): Entity instance
            component (BaseComponent): Component that subclasses BaseComponent
        """
        # components array can only grow.
        if entity._id >= self.entity_len:
            dif = entity._id - self.entity_len + 1
            for _ in range(dif):
                self.components.append([])
            self.components[entity._id] = []
        else:
            self.components[entity._id].append(component)

    def remove_component(self, entity: Entity, component_type: Component):
        try:
            del self.components[component_type._uid][entity]
        except KeyError:
            raise EntityDoesNotHaveComponent()

    def get_entity_components(self, entity: Entity, component_types: list[Component]):
        # most time is spent here
        # big brain time: What if I did components[entity][comp_type]
        # instead of components[comp_type][entity]
        # LOL
        # wait I also have to change it to use a list so this is kinda useless.
        # FUCK THISSSSS
        # I HATE THIS
        # I HATE OVERSCOPING
        # IM JUST GONNA GO BACK TO THE DICT BASED ONE
        # FUCK THIS, IM OUT
        wanted_components = []
        self.component_manager.get_entity_components()
        return components

    def get_component_types(self):
        for component_type in self.component_types:
            yield component_type
