with open("INPUT.TXT", "r") as f:
    x = int(f.readline())
    win = "GCV"
    for i in range(x):
        win = win[2] + win[0] + win[1]
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(win)