from pygame_ecs.entity import Entity
from pygame_ecs.managers.component_manager import ComponentManager


class EntityManager:
    def __init__(self) -> None:
        self.count = 0
        self.dead_entities: list[Entity] = []

    def add_entity(self):
        if len(self.dead_entities) > 0:
            entity = self.dead_entities.pop()
        else:
            entity = Entity(self.count)
            self.count += 1
        return entity

    def kill_entity(self, component_manager: ComponentManager, entity: Entity):
        self.dead_entities.append(entity)
        for component_type in component_manager.components.keys():
            try:
                del component_manager.components[component_type][entity]
            except KeyError:
                pass
