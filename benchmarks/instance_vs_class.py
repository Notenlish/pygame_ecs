import timeit


class Instance:
    def __init__(self, x: int) -> None:
        self.x = x


class _Class:
    x: int


K = 5_000
N = 10_000

# I tested this with both assignment, getting, and doing both
# Instance *is* faster. By a huge metric(at least 20%)


def test_normal():
    instance = Instance(1)
    for k in range(K):
        instance.x = 1
        for n in range(N):
            instance.x = 2


def test_class():
    _class = _Class
    for k in range(K):
        _class.x = 1
        for n in range(N):
            _class.x = 2


instance_time = timeit.timeit(test_normal, number=1)
class_time = timeit.timeit(test_class, number=1)

print("Instance:", instance_time)
print("Class:", class_time)
print(f"Class is faster than Instance by: {instance_time / class_time}")
