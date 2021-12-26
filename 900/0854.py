result = 0
with open("INPUT.TXT", "r") as f:
    t1, t2 = map(int, f.readline().split())
    mode = f.readline()
    if mode == "heat":
        result = max(t1, t2)
    if mode == "freeze":
        result = min(t1, t2)
    if mode == "auto":
        result = t2
    if mode == "fan":
        result = t1
with open("OUTPUT.TXT", "w") as f:
    f.write(str(result))

# TODO: wtf wrong answer