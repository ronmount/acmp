up, down = 0, 0
with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    for i in range(n):
        if int(f.readline()) == 0:
            up += 1
        else:
            down += 1
with open("OUTPUT.TXT", "w") as f:
    f.write(str(min(up, down)))