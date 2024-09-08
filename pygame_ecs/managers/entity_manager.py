from pygame_ecs.entity import Entity
from pygame_ecs.managers.component_manager import ComponentManager


class EntityManager:
    __slots__ = ("component_manager", "entities", "dead_entities", "_limbo", "count")

    def __init__(self, component_manager: ComponentManager) -> None: ...

    def create_entity(self):
        """Creates an entity."""
        ...

    def kill_entity(self, entity: Entity):
        """Kills an entity by moving it into `limbo`. Entities in limbo is removed from  entities once ._clear_limbo is called.
        NOTE: ._clear_limbo is called automatically when all of the active systems are done updating.

        Args:
            entity (Entity): an Entity object

        Raises:
            `EntityAlreadyInLimbo`: An entity is already in limbo(already has been killed)
        """
        ...

    def _clear_limbo(self):
        """Function to get rid of entities that have been killed that frame.
        You probably won't need to call this yourself, it will be called automatically.
        """
        ...
