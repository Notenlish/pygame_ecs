from timeit import timeit
import pygame_ecs
import random

WIDTH = 800
HEGIHT = 800
ENTITY_AMOUNT = 1_000 * 10


class Position(pygame_ecs.BaseComponent):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class Velocity(pygame_ecs.BaseComponent):
    def __init__(self, vec: list[int | float]) -> None:
        super().__init__()
        self.vec = vec


class BallPhysics(pygame_ecs.BaseSystem):
    def __init__(self) -> None:
        super().__init__(required_component_types=[Position, Velocity])
        self.dt = 0

    def update(self, entity_components):
        pos: Position = entity_components[Position]  # type: ignore
        vel: Velocity = entity_components[Velocity]  # type: ignore
        pos.x += vel.vec[0]  # type: ignore
        pos.y += vel.vec[1]  # type: ignore
        if pos.x > WIDTH or pos.x < 0:
            vel.vec[0] *= -1
        if pos.y > HEGIHT or pos.y < 0:
            vel.vec[1] *= -1


entities = []
entity_manager = pygame_ecs.EntityManager()
component_manager = pygame_ecs.ComponentManager()
system_manager = pygame_ecs.SystemManager()
ball_physics = BallPhysics()

component_manager.add_component_type(Position)
component_manager.add_component_type(Velocity)

for _ in range(ENTITY_AMOUNT):
    center = (
        random.randint(0, WIDTH),
        random.randint(0, HEGIHT),
    )
    radius = random.randint(2, 12)
    color = [random.randint(0, 255) for _ in range(3)]
    vel = [
        (random.random() - 0.5) * 400 / 1000,
        (random.random() - 0.5) * 400 / 1000,
    ]
    entity = entity_manager.add_entity(component_manager)
    component_manager.add_component(entity, Position(center[0], center[1]))
    component_manager.add_component(entity, Velocity(vel))
    entities.append(entity)


REPEAT = 1_000

res = timeit(lambda: system_manager.update_entities(entities, component_manager, ball_physics), number=REPEAT)  # type: ignore
print(f"Took {res/REPEAT} roughly for each frame, using {ENTITY_AMOUNT} entities")
