with open("INPUT.TXT", "r") as f:
    tmp = list(map(int, f.readline().split(" ")))
    a, b = tmp[:3], tmp[3:]
    result = max(a) * max(b) + min(a) * min(b) + (sum(a) - max(a) - min(a)) * (sum(b) - max(b) - min(b))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(result))
