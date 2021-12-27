with open("INPUT.TXT", "r") as f:
    f.readline()
    n = list(map(int, f.readline().split()))
    with open("OUTPUT.TXT", "w") as q:
        q.write(f"{min(n)} {max(n)}")