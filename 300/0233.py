with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    b = list(map(int, f.readline().split()))
    result = "No crash"
    for i in b:
        if i <= 437:
            result = f"Crash {b.index(i) + 1}"
            break
    with open("OUTPUT.TXT", "w") as q:
        q.write(result)