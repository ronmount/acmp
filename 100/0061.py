a, b = 0, 0
with open("INPUT.TXT", "r") as f:
    for _ in range(4):
        c = list(map(int, f.readline().split(" ")))
        a += c[0]
        b += c[1]
with open("OUTPUT.TXT", "w") as f:
    if a > b:
        f.write("1")
    elif a < b:
        f.write("2")
    else:
        f.write("DRAW")
