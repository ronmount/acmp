with open("INPUT.TXT", "r") as f:
    a = int(f.readline())
    with open("OUTPUT.TXT", "w") as f1:
        if a in [12, 1, 2]:
            f1.write("Winter")
        elif a in [3, 4, 5]:
            f1.write("Spring")
        elif a in [6, 7, 8]:
            f1.write("Summer")
        elif a in [9, 10, 11]:
            f1.write("Autumn")
        else:
            f1.write("Error")