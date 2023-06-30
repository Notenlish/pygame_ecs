import typing

from pygame_ecs.components.base_component import BaseComponent
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import EntityDoesNotHaveComponent


ComponentInstanceType = typing.TypeVar("ComponentInstanceType", bound=BaseComponent)


class ComponentManager:
    __slots__ = ("components",)
    def __init__(self) -> None:
        self.components: dict[typing.Type[BaseComponent], dict[Entity, ComponentInstanceType]] = {}  # type: ignore

    def init_components(self):
        # get all subclasses using BaseComponent
        component_subclasses = BaseComponent.__subclasses__()
        for component_subclass in component_subclasses:
            self.components[component_subclass] = {}

    def add_component(self, entity, component):
        """Adds a component to an entity

        Args:
            entity (Entity): Entity instance
            component (BaseComponent): Component that subclasses BaseComponent
        """
        self.components[type(component)][entity] = component

    def remove_component(self, entity, component_type):
        try:
            del self.components[component_type][entity]
        except KeyError:
            raise EntityDoesNotHaveComponent(entity, component_type)
