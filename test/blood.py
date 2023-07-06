# Modified version of code created by kirro_yt from discord

import pygame
import pygame_ecs
import random
import time
import math

from pygame_ecs.components.base_component import BaseComponent
from pygame_ecs.entity import Entity

start = time.time()

WIDTH = 800
HEIGHT = 600


class Position(pygame_ecs.BaseComponent):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class BallRenderer(pygame_ecs.BaseComponent):
    def __init__(self, radius: int, color) -> None:
        super().__init__()
        self.radius = radius
        self.color = color


class Velocity(pygame_ecs.BaseComponent):
    def __init__(
        self, vel: pygame.math.Vector2, time_offset: float | int, wave_length: float
    ) -> None:
        super().__init__()
        self.vel: pygame.math.Vector2 = vel
        self.time_offset = time_offset
        self.wave_length = wave_length


class BallDrawSystem(pygame_ecs.BaseSystem):
    def __init__(self, screen) -> None:
        super().__init__(required_component_types=[Position, BallRenderer])
        self.screen = screen

    def update_entity(self, entity, entity_components):
        pos: Position = entity_components[Position]
        ball_renderer: BallRenderer = entity_components[BallRenderer]
        pygame.draw.circle(
            self.screen, ball_renderer.color, (pos.x, pos.y), ball_renderer.radius
        )


class BallPhysics(pygame_ecs.BaseSystem):
    def __init__(self, dt) -> None:
        super().__init__(required_component_types=[Position, Velocity, BallRenderer])
        self.dt = dt

    def update_entity(self, entity: Entity, entity_components):
        pos: Position = entity_components[Position]
        velocity: Velocity = entity_components[Velocity]
        ball_renderer: BallRenderer = entity_components[BallRenderer]
        pos.y += (
            math.sin(time.time() - start + velocity.time_offset)
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

component_manager = pygame_ecs.ComponentManager()
entity_manager = pygame_ecs.EntityManager(component_manager)
system_manager = pygame_ecs.SystemManager(entity_manager, component_manager)
ball_draw_system = BallDrawSystem(screen)
ball_physics_system = BallPhysics(dt=0)
system_manager.add_system(ball_draw_system)
system_manager.add_system(ball_physics_system)
component_manager.init_components()

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
    entity = entity_manager.add_entity()
    component_manager.add_component(entity, Position(center[0], center[1]))
    component_manager.add_component(entity, BallRenderer(radius, color))
    component_manager.add_component(entity, velocity)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    ball_physics_system.dt = clock.get_time() / 1000
    system_manager.update_entities()
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
