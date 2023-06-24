from pygame_ecs.entity import Entity
from pygame_ecs.managers.component_manager import ComponentManager


class EntityManager:
    def __init__(self) -> None:
        self.count = 0
        self.dead_entities: list[Entity] = []

    def add_entity(self, component_manager: ComponentManager):
        if len(self.dead_entities) > 0:
            entity = Entity(self.dead_entities.pop())
            component_manager.components[entity] = []
            return entity
        else:
            entity = Entity(self.count)
            self.count += 1
        component_manager.components[entity] = []
        return entity

    def kill_entity(self, component_manager: ComponentManager, entity: Entity):
        self.dead_entities.append(entity)
        component_manager.components[entity] = []  # clear components
