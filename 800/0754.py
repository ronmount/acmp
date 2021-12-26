with open("INPUT.TXT", "r") as f:
    a = list(map(int, f.readline().split(" ")))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(max(a)) if max(a) <= 727 and min(a) >= 94 else "Error")