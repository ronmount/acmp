with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    with open("OUTPUT.TXT", "w") as f1:
        for i in range(n):
            n, m = map(int, f.readline().split(" "))
            f1.write(str(19 * m + (n + 239) * (n + 366) // 2))
            f1.write("\n")