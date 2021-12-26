with open('INPUT.TXT', 'r') as f:
    nums = list(map(int, f.readline().split()))
    k = nums[0]
    n = nums[1]
    arr = [1]

    for i in range(1, n + 1):
        arr.append(sum(arr[max(0, i-k):i]))

    with open('OUTPUT.TXT', 'w') as o:
        o.write(str(arr[n]))
