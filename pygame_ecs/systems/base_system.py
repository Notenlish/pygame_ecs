from pygame_ecs.components.base_component import BaseComponent


class BaseSystem:
    def __init__(self, required_component_types: list[BaseComponent]) -> None:
        self.required_component_types = required_component_types

    def update(self):
        pass
