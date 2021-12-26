with open("INPUT.TXT", "r") as f:
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(int(f.readline()) + 1))