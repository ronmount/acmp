with open("INPUT.TXT", "r") as f:
    a = f.readline()
    with open("OUTPUT.TXT", "w") as f1:
        f1.write("YES" if a[:2] == a[3] + a[2] else "NO")
