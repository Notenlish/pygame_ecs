class BaseComponent:
    """An Base class that all Components must inherit from."""

    def __init__(self) -> None:
        pass

    def __repr__(self):
        return f"<Component {type(self).__name__}>"

    def __str__(self):
        return f"<Component {type(self).__name__}>"
