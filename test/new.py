import pygame
from pygame_ecs.components.base import Component
from pygame_ecs.entity import Entity
from pygame_ecs.systems.base_system import System
from pygame_ecs.ecs import ECS

window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ecs = ECS()
dt = 0


class Position(Component):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class Ball(Component):
    def __init__(self, radius: float, color: str | tuple[int, int, int]) -> None:
        super().__init__()
        self.radius = radius
        self.color = color


class BallDrawer(System):
    def __init__(self) -> None:
        super().__init__(required_component_types=[Position, Ball])

    def update_entity(self, entity: Entity, entity_components):
        position: Position = entity_components[0]
        ball: Ball = entity_components[1]
        pygame.draw.circle(window, ball.color, (position.x, position.y), ball.radius)


entity = ecs.create_entity()
ecs.add_component(entity, Position(100, 100))
ecs.add_component(entity, Ball(50, "red"))
ecs.add_system(BallDrawer())

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit

    ecs.update()

    dt = clock.tick(60)
    pygame.display.flip()
