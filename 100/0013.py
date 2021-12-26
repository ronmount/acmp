bulls, cows = 0, 0
with open("INPUT.TXT", "r") as f:
    s1, s2 = f.readline().split(" ")
    for i in range(4):
        if s1[i] == s2[i]:
            bulls += 1
        elif s2[i] in s1:
            cows += 1
with open("OUTPUT.TXT", "w") as f:
    f.write(f"{bulls} {cows}")