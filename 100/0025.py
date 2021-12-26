with open("INPUT.TXT", "r") as f:
    a, b = int(f.readline()), int(f.readline())
    with open("OUTPUT.TXT", "w") as f1:
        if a > b:
            f1.write(">")
        elif a < b:
            f1.write("<")
        else:
            f1.write("=")