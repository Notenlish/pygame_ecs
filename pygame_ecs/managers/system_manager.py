import typing

from pygame_ecs.systems.base_system import BaseSystem
from pygame_ecs.components.base_component import BaseComponent
from pygame_ecs.managers.component_manager import ComponentManager

SystemType = typing.TypeVar("SystemType", bound=BaseSystem)


class SystemManager:
    def __init__(self) -> None:
        self.systems: list[BaseSystem] = []

    def add_system(self, system: BaseSystem):
        self.systems.append(system)

    def remove_system(self, system: BaseSystem):
        self.systems.remove(system)

    def update_entities(
        self, entities, component_manager: ComponentManager, system: SystemType
    ):
        for entity in entities:
            has_components = True
            components_to_give = {}
            for comp_type in system.required_component_types:
                try:
                    comp = component_manager.components[comp_type][entity]
                    components_to_give[type(comp)] = comp
                except KeyError:
                    has_components = False
                    break
            if has_components:
                system.update(components_to_give)
