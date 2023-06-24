import typing

from pygame_ecs.components.base_component import BaseComponent
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import EntityDoesNotHaveComponent, EntityHasNoComponents


class ComponentManager:
    def __init__(self) -> None:
        self.components: dict[Entity, list[typing.Type[BaseComponent]]] = {}
        # TODO: try changing the structure to:
        # self.components: dict[ComponentType, dict[Entity, Component(instance)]]

    def add_component(self, entity, component):
        _dict = self.components.get(entity, [])
        _dict.append(component)
        self.components[entity] = _dict

    def remove_component(self, entity, component_type):
        try:
            comp_list = self.components[entity]
            for i, component in enumerate(comp_list):
                if type(component) == component_type:
                    comp_list.pop(i)
                    return None
            raise EntityDoesNotHaveComponent(entity, component_type)
        except KeyError:  # havent added any components to entity
            raise EntityHasNoComponents(entity)
        except KeyboardInterrupt:
            pass
