import re

with open('../INPUT.TXT', 'r') as f:
    l = f.readline()[0:5]
    c2n = {"A": 1, "B": 2, "C": 3, "D": 4,
                "E": 5, "F": 6, "G": 7, "H": 8}
    if re.match("[A-H][1-8]-[A-H][1-8]", l):
        search = re.search("([A-H])([1-8])-([A-H])([1-8])", l)
        c1 = c2n[search.group(1)]
        n1 = int(search.group(2))
        c2 = c2n[search.group(3)]
        n2 = int(search.group(4))
        if abs(c1-c2) + abs(n1-n2) == 3 and abs(c1-c2) > 0 and abs(n1-n2) > 0:
            result = "YES"
        else:
            result = "NO"
    else:
        result = "ERROR"
    with open('../OUTPUT.TXT', 'w') as o:
        o.write(result)