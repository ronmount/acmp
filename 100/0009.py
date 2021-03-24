with open('../INPUT.TXT', 'r') as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
    sum = sum(list(filter(lambda x: x > 0, nums)))
    mult = 1
    min_index = nums.index(min(nums))
    max_index = nums.index(max(nums))
    for num in nums[min(min_index, max_index) + 1:max(min_index, max_index)]:
        mult *= num
    with open('../OUTPUT.TXT', 'w') as o:
        o.write(f"{sum} {mult}")