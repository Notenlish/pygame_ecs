
import subprocess
import sys


for _ in range(5):
    val = subprocess.run("py test/speed_test.py perfect")
    val = subprocess.run("py test/speed_test.py notperfect")

