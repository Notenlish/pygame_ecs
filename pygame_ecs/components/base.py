class Component:
    _uid = 0
    """An Base class that all Components must inherit from.
    Make sure to specify the __slots__ attribute in your subclasses for increased performance.
    See https://wiki.python.org/moin/UsingSlots for more details."""

    def __init__(self) -> None:
        pass

    def __repr__(self):
        return f"<Component {type(self).__name__}>"

    def __str__(self):
        return f"<Component {type(self).__name__}>"
