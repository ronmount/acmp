with open("INPUT.TXT", "r") as f:
    a, b, c, t = map(int, f.readline().split())
    if t > a:
        result = a * b + (t - a) * c
    else:
        result = b * t
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(result))