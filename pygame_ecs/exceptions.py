class EntityDoesNotHaveComponent(Exception):
    def __init__(self, entity, component_type) -> None:
        msg = f"Entity of id {entity} doesn't have component of type {component_type} that can be accessed."
        super().__init__(msg)


class EntityAlreadyInLimbo(Exception):
    def __init__(self, entity) -> None:
        msg = f"{entity} is already in limbo(has been killed before)"
        super().__init__(msg)
