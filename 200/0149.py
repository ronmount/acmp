with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split(" ")))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(" ".join(map(str, a[::-1])))
    # TODO: runtime error ??
