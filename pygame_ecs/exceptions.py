class EntityDoesNotHaveComponent(Exception):
    def __init__(self, entity, component_type) -> None:
        msg = f"Entity of id {entity} doesn't have component of type {component_type} that can be accessed."
        super().__init__(msg)
