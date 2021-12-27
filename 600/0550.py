with open("INPUT.TXT", "r") as f:
    x = int(f.readline())
    r = f"1{2 + int(not((x % 4 == 0 and x % 100 != 0) or x % 400 == 0))}/09/{str(x).zfill(4)}"
    with open("OUTPUT.TXT", "w") as q:
        q.write(r)