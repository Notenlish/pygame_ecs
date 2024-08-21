import subprocess
import sys

for _ in range(5):
    subprocess.run("py test/speed_test_old.py perfect")
print()
for _ in range(5):
    subprocess.run("py test/speed_test_old.py imperfect")
