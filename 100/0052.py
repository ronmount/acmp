with open("INPUT.TXT", "r") as f:
    s = list(f.readline())
    h1 = list(map(int, s[:3]))
    h2 = list(map(int, s[3:]))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write("YES" if sum(h1) == sum(h2) else "NO")
# TODO: runtime error ??