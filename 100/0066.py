result = ''
with open("INPUT.TXT", "r") as f:
    char = f.readline()
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for i in range(len(rows)):
        if char in rows[i]:
            if char == rows[i][-1]:
                result = rows[(i + 1) % 3][0]
            else:
                result = rows[i][rows[i].index(char) + 1]
with open("OUTPUT.TXT", "w") as f:
    f.write(result)
# TODO: Presentation error??????