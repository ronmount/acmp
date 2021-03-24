with open('../INPUT.TXT', 'r') as f:
    nums = f.readline().split(" ")
    with open('../OUTPUT.TXT', 'w') as o:
        o.write("YES" if int(nums[0]) * int(nums[1]) == int(nums[2]) else "NO")