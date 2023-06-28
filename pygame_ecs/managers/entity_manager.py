from pygame_ecs.entity import Entity
from pygame_ecs.managers.component_manager import ComponentManager
from pygame_ecs.exceptions import EntityAlreadyInLimbo


class EntityManager:
    def __init__(self, component_manager: ComponentManager) -> None:
        self.component_manager = component_manager
        self.entities: dict[Entity, None] = {}
        self.dead_entities: list[Entity] = []
        self._limbo: dict[Entity, None] = {}
        self.count: int = 0

    def add_entity(self):
        if len(self.dead_entities) > 0:
            entity = self.dead_entities.pop()
        else:
            entity = Entity(self.count)
            self.count += 1
        self.entities[entity] = None
        return entity

    def kill_entity(self, entity: Entity):
        """Kills an entity by moving it into `limbo`. Entities in limbo is removed from  entities once ._clear_limbo is called.
        NOTE: ._clear_limbo is called automatically when all of the active systems are done updating.

        Args:
            entity (Entity): an Entity object

        Raises:
            EntityAlreadyInLimbo: An entity is already in limbo(already has been killed)
        """
        try:
            self._limbo[entity]
            raise EntityAlreadyInLimbo(entity)
        except KeyError:  # not in limbo
            self._limbo[entity] = None
        for component_type in self.component_manager.components.keys():
            try:
                del self.component_manager.components[component_type][entity]
            except KeyError:
                pass

    def _clear_limbo(self):
        """Function to get rid of entities that have been killed that frame.
        You probably won't need to call this yourself, it will be called automatically.
        """
        for entity, _ in self._limbo.items():
            self.dead_entities.append(entity)
            del self.entities[entity]
        self._limbo = {}
