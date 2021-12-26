with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    whole_file = f.read()
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(f"{whole_file.count('1') // 2}")
