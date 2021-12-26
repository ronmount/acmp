count = 0

with open("INPUT.TXT") as f:
    n = int(f.readline())
    for _ in range(n):
        x, y, x1, y1, x2, y2, x3, y3, x4, y4 = map(int, f.readline().split())
        if (x, y) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
            count += 1
        else:
            pass
            # TODO: idk lol
            # https://forum.ixbt.com/topic.cgi?id=26:37687
