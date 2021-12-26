import math

with open("INPUT.TXT", "r") as f:
    x1, y1, x2, y2 = map(int, f.readline().split())
    x, y = x2 - x1, y2 - y1
    length = math.sqrt(x * x + y * y)
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(int(length)) if int(length) == length else "%.5f" % length)
