from pygame_ecs.components.base_component import BaseComponent
from pygame_ecs.entity import Entity
from pygame_ecs.exceptions import (EntityDoesNotHaveComponent,
                                   EntityHasNoComponents)


class ComponentManager:
    def __init__(self) -> None:
        self.components: dict[Entity, list[BaseComponent]] = {}

    def add_component(self, entity, component_type):
        val = self.components.get(entity, []).append(component_type)
        self.components[entity] = val

    def remove_component(self, entity, component_type):
        try:
            comp_list = self.components[entity]
            for i, component in enumerate(comp_list):
                if type(component) == component_type:
                    comp_list.pop(i)
                    return None
            raise EntityDoesNotHaveComponent(
                entity=entity, component_type=component_type
            )
        except KeyError:  # havent added any components to entity
            raise EntityHasNoComponents
        except KeyboardInterrupt:
            pass
