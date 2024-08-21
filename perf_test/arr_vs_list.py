import array
from timeit import timeit
import matplotlib.pyplot as plt

VALUES = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]
REPEAT_NUM = 1_000


def test(N):
    normal = [i for i in range(N)]
    arr = array.array("I", [i for i in range(N)])

    def test_normal():
        new = []
        for i in normal:
            new.append(i + 1)

    def test_arr():
        new = []
        for i in arr:
            new.append(i + 1)

    normal_time = timeit(test_normal, number=REPEAT_NUM)
    array_time = timeit(test_arr, number=REPEAT_NUM)

    return {
        "normal": {"total": normal_time, "avg": normal_time / N},
        "array": {"total": array_time, "avg": array_time / N},
    }


data = []
for N in VALUES:
    out = test(N)
    data.append([out["normal"]["total"], out["array"]["total"]])

# Transpose the list to get times for normal and array separately
data = list(zip(*data))
normal_times = data[0]
array_times = data[1]

plt.plot(VALUES, normal_times, marker="o", label="Normal List")
plt.plot(VALUES, array_times, marker="o", label="Array")

plt.xlabel("Number of Elements (N)")
plt.ylabel("Total Time (seconds)")
plt.title("Performance Comparison: List vs Array(lower better)")
plt.legend()
plt.grid(True)
plt.show()
