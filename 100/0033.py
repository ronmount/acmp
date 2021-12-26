with open("INPUT.TXT", "r") as f:
    a, b = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(f"{a + b - 1 - a} {a + b - 1 - b}")