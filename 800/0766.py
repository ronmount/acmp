with open("INPUT.TXT", "r") as f:
    a, b, c = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write("YES" if a * b >= c else "NO")