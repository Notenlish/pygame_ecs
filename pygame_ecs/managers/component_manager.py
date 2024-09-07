import typing

from pygame_ecs.components.base_component import Component
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import EntityDoesNotHaveComponent

ComponentInstanceType = typing.TypeVar("ComponentInstanceType", bound=Component)


class ComponentManager:
    __slots__ = ("components",)

    def __init__(self) -> None:
        self.components: dict[
            typing.Type[Component], dict[Entity, ComponentInstanceType]
        ] = {}

    def init_components(self):
        # get all subclasses using BaseComponent
        component_subclasses = Component.__subclasses__()
        uid = 0
        for component_subclass in component_subclasses:
            component_subclass._uid = uid
            self.components[uid] = {}
            uid += 1

    def add_component(self, entity, component: type[Component]):
        """Adds a component to an entity

        Args:
            entity (Entity): Entity instance
            component (BaseComponent): Component that subclasses BaseComponent
        """
        self.components[component._uid][entity] = component

    def remove_component(self, entity, component_type: type[Component]):
        try:
            del self.components[component_type._uid][entity]
        except KeyError:
            raise EntityDoesNotHaveComponent(entity, component_type)
