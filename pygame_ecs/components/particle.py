from typing import Iterable

from pygame import Vector2, Surface
from pygame_ecs.components.base import Component


class Particle(Component):
    def __init__(self, pos: Vector2 | Iterable[int | float], surface: Surface) -> None:
        if type(pos) is Vector2:
            self.pos = pos
        else:
            self.pos = Vector2(*pos)

        self.surface = surface


class CircleShape(Component):
    def __init__(self, radius:float) -> None:
        ...
