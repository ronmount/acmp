with open('INPUT.TXT', 'r') as f:
    nums = list(map(int, f.readline().split()))
    result = list()
    for x in range(-100, 101):
        if nums[0] * x * x * x + nums[1] * x * x + \
                nums[2] * x + nums[3] == 0:
            result.append(x)
    with open('OUTPUT.TXT', 'w') as o:
        o.write(' '.join(map(str, sorted(result))))