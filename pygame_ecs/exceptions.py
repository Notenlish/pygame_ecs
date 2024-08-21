class EntityDoesNotHaveComponent(Exception):
    def __init__(self) -> None:
        super().__init__()


class EntityAlreadyInLimbo(Exception):
    def __init__(self) -> None:
        super().__init__()
