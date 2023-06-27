# Pygame_ecs

An Pure Python, simple to use ECS library for pygame.

## How it works

Create an entity

```python
entities = []
entity = entity_manager.add_entity(component_manager)
entities.append(entity)
```

You can delete an entity like this:
```python
    entity = entities[random.randint(0, len(entities) - 1)]
    entity_manager.kill_entity(component_manager, entity)
    entities.remove(entity)
```

Components are just classes that hold data

```python
class Position(pygame_ecs.BaseComponent):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y
```

Systems are just classes that hold logic

```python

class BallPhysics(pygame_ecs.BaseSystem):
    def __init__(self, screen) -> None:
        super().__init__(required_component_types=[Position, Velocity])
        self.dt = 0
        self.screen = screen

    def update(self, entity_components):
        pos: Position = entity_components[Position]
        vel: Velocity = entity_components[Velocity]
        pos.x += vel.vec.x * self.dt
        pos.y += vel.vec.y * self.dt
        if pos.x > WIDTH or pos.x < 0:
            vel.vec.x *= -1
        if pos.y > HEIGHT or pos.y < 0:
            vel.vec.y *= -1


```

## Example Usage
```py

import pygame
import pygame_ecs
import random

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

class BallDrawSystem(pygame_ecs.BaseSystem):
    def __init__(self, screen) -> None:
        super().__init__(required_component_types=[Position, BallRenderer])
        self.screen = screen

    def update(self, entity_components):
        pos: Position = entity_components[Position]
        ball_renderer: BallRenderer = entity_components[BallRenderer]
        pygame.draw.circle(
            self.screen, ball_renderer.color, (pos.x, pos.y), ball_renderer.radius
        )

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

entity_manager = pygame_ecs.EntityManager()
component_manager = pygame_ecs.ComponentManager()
system_manager = pygame_ecs.SystemManager()
ball_draw_system = BallDrawSystem(screen)
component_manager.init_components()

entities = []
for _ in range(100):
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
    entity = entity_manager.add_entity(component_manager)
    component_manager.add_component(entity, Position(center[0], center[1]))
    component_manager.add_component(entity, BallRenderer(radius, color))
    entities.append(entity)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    system_manager.update_entities(entities, component_manager, ball_draw_system)
    pygame.display.update()
    clock.tick(60)
    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
```

## Credits

I'd like to give credit to https://www.youtube.com/watch?v=71RSWVyOMEY and https://github.com/seanfisk/ecs
As well as `dickerdackel` from pgc server and `SamieZaurus#8030` from UnitOfTime's server.
