import typing

from pygame_ecs.components.base_component import BaseComponent
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import EntityDoesNotHaveComponent


ComponentInstanceType = typing.TypeVar("ComponentInstanceType", bound=BaseComponent)


class ComponentManager:
    def __init__(self) -> None:
        self.components: dict[typing.Type[BaseComponent], dict[Entity, ComponentInstanceType]] = {}  # type: ignore
        # TODO: try changing the structure to:
        # self.components: dict[ComponentType, dict[Entity, Component(instance)]]

    def add_component_type(self, component_type):
        self.components[component_type] = {}

    def remove_component_type(self, component_type):
        del self.components[component_type]

    def add_component(self, entity, component):
        self.components[type(component)][entity] = component

    def remove_component(self, entity, component_type):
        try:
            del self.components[component_type][entity]
        except KeyError:
            raise EntityDoesNotHaveComponent(entity, component_type)
