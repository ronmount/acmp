with open("INPUT.TXT", "r") as f:
    k, m = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(k * k * m))