with open("INPUT.TXT", "r") as f:
    r1, r2, r3 = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write("YES" if r2 + r3 <= r1 else "NO")