class Component:
    # pygame_ecs automatically sets uid for classes so instead of hashing
    # the whole class python can just hash this attribute
    _uid = None
    """An Base class that all Components must inherit from.
    Make sure to specify the __slots__ attribute in your subclasses for increased performance.
    See https://wiki.python.org/moin/UsingSlots for more details."""

    def __repr__(self):
        return f"<Component {type(self).__name__}>"

    def __str__(self):
        return f"<Component {type(self).__name__}>"
