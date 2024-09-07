from pygame_ecs.backends.list import ListBackend
from pygame_ecs.backends.base import BaseBackend


class ComponentManager:
    # TODO: remove this
    __slots__ = ("backend",)

    def __init__(self, backend_type: type[BaseBackend] = None) -> None:
        self.backend = ListBackend(self) if backend_type is None else backend_type

    def get_entity_components(self, entity, component_types):
        components = self.backend.get_entity_components(entity, component_types)
        return components

    def get_component_types(self):
        return self.backend.get_component_types()

    def init_components(self):
        self.backend.init_components()

    def _add_component_type(self, component_type):
        """Adds a component type. You generally shouldn't need to manually call this if your components are subclasses of BaseComponent"""
        self.backend._add_component_type(component_type)

    def add_component(self, entity, component):
        self.backend.add_component(entity, component)

    def remove_component(self, entity, component_type):
        self.backend.remove_component(entity, component_type)
