with open("INPUT.TXT", "r") as f:
    a = int(f.readline())
    is_binary = False
    for i in range(0, 14):
        if a == 2 ** i:
            is_binary = True
            break
    with open("OUTPUT.TXT", "w") as f1:
        f1.write("YES" if is_binary else "NO")
