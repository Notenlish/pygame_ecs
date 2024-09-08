from timeit import timeit

N = 10_000_000


class Thingy:
    def __init__(self, b) -> None:
        self.b = b


class Thingy2:
    a: int


Thingy2.a = 1
instance = Thingy(2)

class_time = timeit(lambda: Thingy2.a, number=N)
instance_time = timeit(lambda: instance.b, number=N)

print("class", class_time)
print("instance", instance_time)
print(f"instance faster than class by: {class_time/instance_time:.5f}")
