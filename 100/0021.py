with open("INPUT.TXT", "r") as f:
    salaries = list(map(int, f.readline().split(" ")))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(max(salaries) - min(salaries)))
