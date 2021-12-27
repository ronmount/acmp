with open("INPUT.TXT", "r") as f:
    x = int(f.readline())
    s = 0
    i = 1
    while i * i < x:
        if x % i == 0:
            s += i + x // i
        if i * i == x:
            s += i
        i += 1
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(s))