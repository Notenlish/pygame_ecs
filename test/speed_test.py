import ez_profile

import random
from sys import argv
from timeit import timeit

import pygame_ecs

try:
    arg = argv[1]
    if arg != "perfect":
        arg = "imperfect"
except IndexError:
    arg = "perfect"

WIDTH = 800
HEIGHT = 800
ENTITY_AMOUNT = 1_000 * 4

# TODO: put entities as a list in entity_manager
# Also make the component manager be kept as a reference in the system_manager
# I can insert EntityManager reference into BaseSystem Subclasses using the same method I've used with components nvm i cant lol
# actually add the systems into


class Position(pygame_ecs.BaseComponent):
    __slots__ = ("x", "y")
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class Velocity(pygame_ecs.BaseComponent):
    __slots__ = ("vec",)
    def __init__(self, vec: list[int | float]) -> None:
        super().__init__()
        self.vec = vec


class BallPhysics(pygame_ecs.BaseSystem):
    def __init__(self) -> None:
        super().__init__(required_component_types=[Position, Velocity])

    def update_entity(self, entity, entity_components):
        pos: Position = entity_components[0]  # type: ignore
        vel: Velocity = entity_components[1]  # type: ignore
        pos.x += vel.vec[0]  # type: ignore
        pos.y += vel.vec[1]  # type: ignore
        if pos.x > WIDTH or pos.x < 0:
            vel.vec[0] *= -1
        if pos.y > HEIGHT or pos.y < 0:
            vel.vec[1] *= -1


component_manager = pygame_ecs.ComponentManager()
entity_manager = pygame_ecs.EntityManager(component_manager)
system_manager = pygame_ecs.SystemManager(entity_manager, component_manager)
ball_physics = BallPhysics()
system_manager.add_system(ball_physics)
component_manager.init_components()

for _ in range(ENTITY_AMOUNT):
    center = (
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
    )
    radius = random.randint(2, 12)
    color = [random.randint(0, 255) for _ in range(3)]
    vel = [
        (random.random() - 0.5) * 400 / 1000,
        (random.random() - 0.5) * 400 / 1000,
    ]
    entity = entity_manager.add_entity()
    component_manager.add_component(entity, Position(center[0], center[1]))
    if arg == "perfect":
        component_manager.add_component(entity, Velocity(vel))

for entity in entity_manager.entities.keys():
    entity_manager.kill_entity(entity)
entity_manager._clear_limbo()

for _ in range(
    ENTITY_AMOUNT + 1_000
):  # ensure that killing and then spawning entities doesnt break anything
    center = (
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
    )
    radius = random.randint(2, 12)
    color = [random.randint(0, 255) for _ in range(3)]
    vel = [
        (random.random() - 0.5) * 400 / 1000,
        (random.random() - 0.5) * 400 / 1000,
    ]
    entity = entity_manager.add_entity()
    component_manager.add_component(entity, Position(center[0], center[1]))
    if arg == "perfect":
        component_manager.add_component(entity, Velocity(vel))

REPEAT = 1_000

result = timeit(lambda: system_manager.update_entities(), number=REPEAT)  # type: ignore
print(
    f"Took a total of {result} and {result/REPEAT} roughly for each frame, using {len(entity_manager.entities)} entities, setting: {arg}"
)
