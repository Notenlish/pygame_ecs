import typing
from pygame_ecs.components.base_component import BaseComponent


class BaseSystem:
    # typing.Type specifies that it will take subclasses of this class
    def __init__(self, required_component_types: list[typing.Type[BaseComponent]]) -> None:
        self.required_component_types = required_component_types

    def update(self, entity_components: list[typing.Type[BaseComponent]]):
        pass

    def __str__(self) -> str:
        return f"<{type(self).__name__}>"
