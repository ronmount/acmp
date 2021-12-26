with open("INPUT.TXT", "r") as f:
    n, a, b = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(n * a * b * 2))