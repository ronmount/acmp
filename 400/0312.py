with open("INPUT.TXT", "r") as f:
    a, b, c = map(int, f.readline().split())
    with open("OUTPUT.TXT", "w") as q:
        q.write(str(a + (b - a)*(c - 1)))