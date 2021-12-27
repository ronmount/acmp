with open("INPUT.TXT", "r") as f:
    x, word = f.readline().split()
    x = int(x)
    with open("OUTPUT.TXT", "w") as q:
        q.write(word[:x-1] + word[x:])