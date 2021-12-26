with open("INPUT.TXT", "r") as f:
    w, h, r = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write("YES" if r*2 <= h and r*2 <= w else "NO")