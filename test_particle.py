from pygame_ecs import ComponentManager, BaseComponent, SystemManager, BaseSystem, Entity, EntityManager

entity_manager = EntityManager()
comp_manager = ComponentManager()

ent1 = entity_manager.add_entity()
comp_manager.add_component(ent1, Position)

