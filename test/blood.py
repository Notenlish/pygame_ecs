# Modified version of code created by kirro_yt from discord

import math
import random
import time

import pygame

from pygame_ecs import Entity, Component, System
from pygame_ecs.ecs.hashmap import HashmapECS

# TODO: implement a particleECS

start = time.time()

WIDTH = 800
HEIGHT = 600


class Position(Component):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class BallRenderer(Component):
    def __init__(self, radius: int, color) -> None:
        super().__init__()
        self.radius = radius
        self.color = color


class Velocity(Component):
    def __init__(
        self, vel: pygame.math.Vector2, time_offset: float | int, wave_length: float
    ) -> None:
        super().__init__()
        self.vel: pygame.math.Vector2 = vel
        self.time_offset = time_offset
        self.wave_length = wave_length


class BallDrawSystem(System):
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        super().__init__(component_types=[Position, BallRenderer])

    def update_entity(self, entity, entity_components):
        # TODO: what matters more? ugly syntax with good performance?
        # OR, good syntax with worse performance?
        pos: Position = entity_components[Position]
        ball_renderer: BallRenderer = entity_components[BallRenderer]
        pygame.draw.circle(
            self.screen, ball_renderer.color, (pos.x, pos.y), ball_renderer.radius
        )


class BallPhysics(System):
    def __init__(self, dt) -> None:
        super().__init__(component_types=[Position, Velocity, BallRenderer])
        self.dt = dt
        self.dif = 0

    def update_entity(self, entity: Entity, entity_components):
        # Use this for strict type checking: pos = cast(Position, entity_components[Position])
        pos: Position = entity_components[Position]
        velocity: Velocity = entity_components[Velocity]
        ball_renderer: BallRenderer = entity_components[BallRenderer]

        pos.y += (
            math.sin(self.dif + velocity.time_offset)
            * (1 / ball_renderer.radius)
            * wave_length
        )
        pos.x += velocity.vel.x * self.dt
        if pos.x > WIDTH + ball_renderer.radius:
            pos.x = -ball_renderer.radius
        if pos.x < -ball_renderer.radius:
            pos.x = WIDTH + ball_renderer.radius


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# component_manager = ComponentManager()
# entity_manager = EntityManager(component_manager)
# system_manager = SystemManager(entity_manager, component_manager)
ecs = HashmapECS()

ball_draw_system = BallDrawSystem(screen)
ball_physics_system = BallPhysics(dt=0)

ecs.add_system(ball_draw_system)
ecs.add_system(ball_physics_system)
ecs.init_components()

for _ in range(2000):
    center = (
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
    )
    radius = random.uniform(6, 15)
    color = [random.randint(0, 255), 0, 0]
    time_offset = random.uniform(0, 2 * math.pi)
    wave_length = random.uniform(1.4, 3)
    velocity = Velocity(
        vel=pygame.math.Vector2(random.randint(30, 50), 0),
        time_offset=time_offset,
        wave_length=wave_length,
    )
    entity = ecs.create_entity()
    ecs.add_component(entity, Position(center[0], center[1]))
    ecs.add_component(entity, BallRenderer(radius, color))
    ecs.add_component(entity, velocity)

while True:
    screen.fill((34, 4, 6))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    ball_physics_system.dt = clock.get_time() / 1000
    ball_physics_system.dif = time.time() - start
    ecs.update_entities()
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
