from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame_ecs.managers.component_manager import ComponentManager

from pygame_ecs.components.base import BaseComponent
from pygame_ecs.exceptions import EntityDoesNotHaveComponent


class BaseBackend:
    """The base backend object all component managers must inherit from.
    Please note that components have unique ids, and you can access it using the `_uid` attribute
    """

    def __init__(self, component_manager: "ComponentManager") -> None:
        self.component_manager = component_manager

    def _init_component(self, component_type: BaseComponent):
        """Override this."""

    def init_components(self):
        component_subclasses = BaseComponent.__subclasses__()
        i = 0
        for component_subclass in component_subclasses:
            component_subclass._uid = i
            self._init_component(component_subclass)
            i += 1

    def _add_component_type(self, component_type):
        """Override this."""

    def add_component(self, entity, component):
        """Override this."""

    def remove_component(self, entity, component_type):
        """Override this."""

    def get_entity_components(self, entity, component_types):
        """Override this."""
    
    def get_component_types(self):
        pass
