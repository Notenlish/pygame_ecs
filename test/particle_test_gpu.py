import random
import typing

import pygame
from pygame._sdl2 import Renderer, Texture, Window, get_drivers

import pygame_ecs
from pygame_ecs.components.base_component import Component

pygame.init()

ENTITY_AMOUNT = 1
WIDTH = 800
HEIGHT = 600


class Position(pygame_ecs.Component):
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class BallRenderer(pygame_ecs.Component):
    __slots__ = ("radius", "color")

    def __init__(self, radius: int, color) -> None:
        super().__init__()
        self.radius = radius
        self.color = color


class Velocity(pygame_ecs.Component):
    __slots__ = "vec"

    def __init__(self, vec: pygame.math.Vector2) -> None:
        super().__init__()
        self.vec = vec


class BallDrawSystem(pygame_ecs.BaseSystem):
    def __init__(self, texture: Texture) -> None:
        super().__init__(required_component_types=[Position, BallRenderer])
        self.texture = texture

    def update_entity(self, entity, entity_components):
        pos: Position = entity_components[Position]  # type: ignore
        ball_renderer: BallRenderer = entity_components[BallRenderer]  # type: ignore

        self.texture.color = ball_renderer.color  # type: ignore
        self.texture.draw(
            None, (pos.x, pos.y, ball_renderer.radius, ball_renderer.radius)
        )


class BallPhysics(pygame_ecs.BaseSystem):
    def __init__(self, screen) -> None:
        super().__init__(required_component_types=[Position, Velocity])
        self.dt = 0
        self.screen = screen

    def update_entity(self, entity, entity_components):
        pos: Position = entity_components[Position]  # type: ignore
        vel: Velocity = entity_components[Velocity]  # type: ignore
        pos.x += vel.vec.x * self.dt  # type: ignore
        pos.y += vel.vec.y * self.dt  # type: ignore
        if pos.x > WIDTH or pos.x < 0:
            vel.vec.x *= -1
        if pos.y > HEIGHT or pos.y < 0:
            vel.vec.y *= -1


def add_entity(component_manager, entity_manager, amount=1):
    for _ in range(amount):
        center = (
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
        )
        radius = random.randint(10, 15)
        color = [random.randint(0, 255) for _ in range(3)]
        color.append(255)
        vel = pygame.math.Vector2(
            (random.random() - 0.5) * 400 / 1000,
            (random.random() - 0.5) * 400 / 1000,
        )
        entity = entity_manager.add_entity()
        component_manager.add_component(entity, Position(center[0], center[1]))
        component_manager.add_component(entity, Velocity(vel))
        component_manager.add_component(entity, BallRenderer(radius, color))


def remove_entity(entity_manager: pygame_ecs.EntityManager, amount=1):
    if len(entity_manager.entities) < amount:
        return
    for _ in range(amount):
        entity = random.choice(list(entity_manager.entities.keys()))
        try:
            entity_manager.kill_entity(entity)
        except pygame_ecs.EntityAlreadyInLimbo:
            pass


class BallAdd(pygame_ecs.BaseSystem):
    def __init__(self, component_manager, entity_manager) -> None:
        super().__init__(required_component_types=[])
        self.component_manager = component_manager
        self.entity_manager = entity_manager

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            add_entity(component_manager, entity_manager, amount=50)
        elif pygame.mouse.get_pressed()[2]:
            remove_entity(entity_manager, amount=50)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
window = Window.from_display_module()


print(list(get_drivers()))
# change based on drivers
renderer = Renderer(window, index=3, accelerated=1)


texture = Texture.from_surface(renderer, pygame.image.load("test/circle.png"))

component_manager = pygame_ecs.ComponentManager()
entity_manager = pygame_ecs.EntityManager(component_manager)
system_manager = pygame_ecs.SystemManager(entity_manager, component_manager)
ball_physics = BallPhysics(screen)
ball_draw_system = BallDrawSystem(texture=texture)
ball_add = BallAdd(component_manager, entity_manager)
system_manager.add_system(ball_draw_system)
system_manager.add_system(ball_physics)
system_manager.add_system(ball_add)
component_manager.init_components()

add_entity(component_manager, entity_manager, amount=ENTITY_AMOUNT)


clock = pygame.time.Clock()
dt = 0

renderer.draw_color = (
    0,
    0,
    0,
    255,
)  # type: ignore
# renderer.draw_color is used for clearing the screen and drawing primitives

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    pygame.display.set_caption(
        f"FPS: {clock.get_fps()} COUNT: {len(entity_manager.entities)}"
    )
    ball_physics.dt = dt
    renderer.clear()
    system_manager.update_entities()
    renderer.present()
    dt = clock.tick(60)

pygame.quit()
