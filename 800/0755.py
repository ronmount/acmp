with open("INPUT.TXT", "r") as f:
    x, y, z = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(x + y - z) if x + y >= z else "Impossible")