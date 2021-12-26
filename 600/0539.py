with open("INPUT.TXT", "r") as f:
    a = int(f.readline())
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(0) if a == 1 else str(a // 2) if a % 2 == 0 else str(a))