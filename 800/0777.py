with open("INPUT.TXT", "r") as f:
    x, y = map(int, f.readline().split())
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(y - x) if y > x else str(y + 12 - x))