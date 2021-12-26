with open('INPUT.TXT', 'r') as f:
    n = f.readline()
    nums = f.readline().split(" ")
    up = [num for num in nums if int(num) % 2]
    down = [num for num in nums if not int(num) % 2]
    with open('OUTPUT.TXT', 'w') as o:
        o.write('\n'.join([' '.join(up), ' '.join(down)]))
        o.write('\nYES' if len(down) >= len(up) else '\nNO')