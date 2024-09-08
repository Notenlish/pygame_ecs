from pygame_ecs.managers.component import ComponentManager
from pygame_ecs.managers.entity import EntityManager
from pygame_ecs.systems.base import System


class SystemManager:
    __slots__ = ("entity_manager", "component_manager", "systems")

    def __init__(
        self, entity_manager: EntityManager, component_manager: ComponentManager
    ) -> None:
        self.entity_manager = entity_manager
        self.component_manager = component_manager
        self.systems: list[System] = []

    def add_system(self, system: System):
        self.systems.append(system)

    def remove_system(self, system: System):
        self.systems.remove(system)

    def update_entities(self):
        """Updates all of the systems that are active.
        NOTE: For updating values of systems, just set their values before calling this function.
        """
        for system in self.systems:
            if len(system.component_types) > 0:
                for entity in self.entity_manager.entities.keys():
                    has_components = True
                    components_to_give = {}
                    for comp_type in system.component_types:
                        try:
                            comp = self.component_manager.components[comp_type._uid][
                                entity
                            ]
                            components_to_give[type(comp)] = comp
                        except KeyError:
                            self.component_manager.components[comp._uid]
                            has_components = False
                            break
                    if has_components:
                        system.update_entity(entity, components_to_give)
            else:
                system.update()
        self.entity_manager._clear_limbo()
