import random


class Class1:
    _uid = 0

    def __init__(self) -> None:
        self.x = random.random()


class Class2:
    _uid = 1

    def __init__(self) -> None:
        self.y = random.randint(-50, 50)


class Class3:
    _uid = 2

    def __init__(self) -> None:
        self.z = bytearray([random.randint(0, 255) for _ in range(255 + 1)])


class Class4:
    _uid = 3

    def __init__(self) -> None:
        self.w = [random.random()] + [random.random() for _ in range(10)]


from timeit import timeit
import matplotlib.pyplot as plt

VALUES = [1_000, 5_000, 10_000, 20_000, 50_000]
REPEAT_NUM = 1_000


def test(N):
    classes = [Class1, Class2, Class3, Class4]
    data = []
    # create values
    for _ in range(N):
        cls_i = round(random.random() * (len(classes) - 1))
        cls = classes[cls_i]
        data.append(cls())

    def test_class():
        # hash class
        test_dict = {}
        for cls in data:
            test_dict[cls] = random.random()

    def test_uid():
        test_dict = {}
        for cls in data:
            test_dict[cls._uid] = random.random()

    class_time = timeit(test_class, number=REPEAT_NUM)
    uid_time = timeit(test_uid, number=REPEAT_NUM)

    return {
        "class": {"total": class_time, "avg": class_time / N},
        "uid": {"total": uid_time, "avg": uid_time / N},
    }


data = []
for N in VALUES:
    out = test(N)
    data.append([out["class"]["total"], out["uid"]["total"]])

# Transpose the list to get times for normal and array separately
data = list(zip(*data))
normal_times = data[0]
array_times = data[1]

plt.plot(VALUES, normal_times, marker="o", label="Class")
plt.plot(VALUES, array_times, marker="o", label="UID")

plt.xlabel("Number of Elements (N)")
plt.ylabel("Total Time (seconds)")
plt.title("Performance Comparison: Class, UID")
plt.legend()
plt.grid(True)
plt.show()
