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
            entity_components: list[
                typing.Type[BaseComponent]
            ] = component_manager.components[entity]
            for required_component in system.required_component_types:
                if required_component not in entity_components:
                    has_components = True
                    break
            if has_components:
                # print(f"System of type {system} updating entity of type {entity}.")
                system.update(
                    entity_components
                )  # there should be a more optimised way of giving the components
