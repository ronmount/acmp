with open('../INPUT.TXT', 'r') as f:
    n = f.readline()
    with open('../OUTPUT.TXT', 'w') as o:
        o.write(str(int(n) * int(n)))