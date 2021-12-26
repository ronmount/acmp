with open("INPUT.TXT", "r") as f:
    a, b, c = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(f"{2 * (a * b + b * c + a * c)} {a * b * c}")