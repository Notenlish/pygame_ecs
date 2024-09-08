import typing

from pygame_ecs.components.base import Component
from pygame_ecs.entity import Entity

ComponentInstanceType = typing.TypeVar("ComponentInstanceType", bound=Component)


class ComponentManager:
    __slots__ = ("components",)

    def __init__(self) -> None:
        self.components

    def init_components(self): ...

    def add_component(self, entity: Entity, component: type[Component]):
        """Adds a component to an entity

        Args:
            entity (Entity): Entity instance
            component (BaseComponent): Component that subclasses BaseComponent
        """
        ...

    def remove_component(self, entity: Entity, component_type: type[Component]):
        """Removes component from an entity.

        Raises `EntityDoesNotHaveComponent` if entity doesn't have component.
        """
        ...
