with open("INPUT.TXT", "r") as f:
    x = f.readline()
    with open("OUTPUT.TXT", "w") as q:
        q.write("YES" if not "0" in x else "NO")