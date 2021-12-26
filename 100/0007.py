with open('INPUT.TXT', 'r') as f:
    with open('OUTPUT.TXT', 'w') as o:
        o.write(str(max([int(i) for i in f.readline().split(" ")])))