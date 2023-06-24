class BaseComponent:
    """An Base class that all Components must inherit from."""

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.__dict__()}"
