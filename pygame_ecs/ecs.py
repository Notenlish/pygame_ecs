from pygame_ecs.systems.base_system import System
from pygame_ecs.components.base import Component
from pygame_ecs.managers.component_manager import ComponentManager
from pygame_ecs.managers.entity_manager import EntityManager, Entity
from pygame_ecs.managers.system_manager import SystemManager
from pygame_ecs.backends.list import ListBackend
from pygame_ecs.backends.base import BaseBackend


class ECS:
    def __init__(self, backend_type: type[BaseBackend] = None) -> None:
        self.component_manager = ComponentManager(backend_type=backend_type)
        self.entity_manager = EntityManager(self.component_manager)
        self.system_manager = SystemManager(self.entity_manager, self.component_manager)

    def add_system(self, system: type[System]):
        self.system_manager.add_system(system)

    def create_entity(self):
        return self.entity_manager.add_entity()

    def add_component(self, entity: Entity, component: type[Component]):
        self.component_manager.add_component(entity, component)

    def kill_entity(self, entity: Entity):
        self.entity_manager.kill_entity(entity)

    def update(self):
        """Updates all of the systems that are active.
        NOTE: For updating values of systems, just set their values before calling this function. Eg: set .dt attribute of a physics system before calling this.
        """
        self.system_manager._update_entities()
