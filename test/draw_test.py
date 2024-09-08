import random

import pygame

import pygame_ecs


class Position(pygame_ecs.Component):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y


class BallRenderer(pygame_ecs.Component):
    def __init__(self, radius: int, color) -> None:
        super().__init__()
        self.radius = radius
        self.color = color


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


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

component_manager = pygame_ecs.ComponentManager()
entity_manager = pygame_ecs.EntityManager(component_manager)
system_manager = pygame_ecs.SystemManager(entity_manager, component_manager)
ball_draw_system = BallDrawSystem(screen)
system_manager.add_system(ball_draw_system)
component_manager.init_components()

for _ in range(200):
    center = (
        random.randint(0, screen.get_width()),
        random.randint(0, screen.get_height()),
    )
    radius = random.randint(4, 18)
    color = [random.randint(0, 255) for _ in range(3)]
    vel = pygame.math.Vector2(
        (random.random() - 0.5) * 400 / 1000,
        (random.random() - 0.5) * 400 / 1000,
    )
    entity = entity_manager.create_entity()
    component_manager.add_component(entity, Position(center[0], center[1]))
    component_manager.add_component(entity, BallRenderer(radius, color))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    system_manager.update_entities()
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
