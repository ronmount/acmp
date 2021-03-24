with open('../INPUT.TXT', 'r') as f:
    num = int(f.readline())
    with open('../OUTPUT.TXT', 'w') as o:
        o.write(f"{num}9{9 - num}")