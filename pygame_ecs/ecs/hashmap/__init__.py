from pygame_ecs.ecs import ECS
from pygame_ecs.ecs.hashmap.managers.entity import EntityManager
from pygame_ecs.ecs.hashmap.managers.component import ComponentManager
from pygame_ecs.ecs.hashmap.managers.system import SystemManager


class HashmapECS(ECS):
    def __init__(self) -> None:
        self.component_manager = ComponentManager()
        self.entity_manager = EntityManager(self.component_manager)
        self.system_manager = SystemManager(self.entity_manager, self.component_manager)

        # this is fun :trollface:
        self.add_component = self.component_manager.add_component
        self.create_entity = self.entity_manager.create_entity
        self.add_system = self.system_manager.add_system
        self.init_components = self.component_manager.init_components
        self.update_entities = self.system_manager.update_entities
