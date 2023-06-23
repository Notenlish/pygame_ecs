

class Entity(object):
    __slots__ = ("_id",)
    def __init__(self, id):
        self._id = id

    def __repr__(self):
        return f"{type(self).__name__} {self._id}"

    def __hash__(self):
        return self._id

    def __eq__(self, other):
        return self._id == hash(other)
