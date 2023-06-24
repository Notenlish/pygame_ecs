from pygame_ecs import ComponentManager, BaseComponent, SystemManager, BaseSystem, Entity, EntityManager

entity_manager = EntityManager()
component_manager = ComponentManager()

class Position(BaseComponent):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

entities = []

ent1 = entity_manager.add_entity(component_manager)
entities.append(ent1)
component_manager.add_component(ent1, Position(10, 20))

ent2 = entity_manager.add_entity(component_manager)
entities.append(ent2)

system_manager = SystemManager()


class TestSystem(BaseSystem):
    def __init__(self) -> None:
        super().__init__(required_component_types=[Position])
    
    def update(self, entity_components):
        for i, comp in enumerate(entity_components):
            if type(comp) == Position:
                pos: Position = comp  # type: ignore
                pos.x += 1

testsystem = TestSystem()

system_manager.add_system(testsystem)

system_manager.update_entities(entities, component_manager, system=testsystem)
