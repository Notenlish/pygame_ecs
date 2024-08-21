import typing

from pygame_ecs.managers.component_manager import ComponentManager
from pygame_ecs.managers.entity_manager import EntityManager
from pygame_ecs.systems.base_system import BaseSystem
from pygame_ecs.exceptions import EntityDoesNotHaveComponent

SystemType = typing.TypeVar("SystemType", bound=BaseSystem)


class SystemManager:
    __slots__ = ("entity_manager", "component_manager", "systems", "components")

    def __init__(
        self, entity_manager: EntityManager, component_manager: ComponentManager
    ) -> None:
        self.entity_manager = entity_manager
        self.component_manager = component_manager
        self.systems: list[BaseSystem] = []

    def add_system(self, system: SystemType):
        system.entity_manager = self.entity_manager
        self.systems.append(system)

    def remove_system(self, system: SystemType):
        self.systems.remove(system)

    def update_entities(self):
        """Updates all of the systems that are active.
        NOTE: For updating values of systems, just set their values before calling this function.
        """
        for system in self.systems:
            if len(system.required_component_types) > 0:
                for entity in self.entity_manager.entities.keys():
                    try:
                        # TODO: Potential problem: Function call overhead
                        # How to fix? Get rid of component manager and do it all on backend???
                        # also TODO: allow multiple ecs's eg: list based ecs for particle systems
                        # sparse set for different kinds of entities with vastly different components etc.
                        # Would require some work though..
                        components = self.component_manager.get_entity_components(
                            entity, system.required_component_types
                        )
                        system.update_entity(entity, components)
                    except EntityDoesNotHaveComponent:
                        continue
            else:
                system.update()
        self.entity_manager._clear_limbo()
