with open('INPUT.TXT', 'r') as f:
    n = int(f.readline())
    with open('OUTPUT.TXT', 'w') as o:
        if n > 0:
            o.write(str(sum(list(range(1, n+1)))))
        else:
            o.write(str(sum(list(range(n, 2)))))