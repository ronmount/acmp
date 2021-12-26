with open("INPUT.TXT", "r") as f:
    a = int(f.readline())
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(f"{a // 6} {a // 6 * 4} {a // 6}")