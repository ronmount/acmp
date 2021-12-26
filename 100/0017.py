with open("INPUT.TXT", "r") as f:
    n = int(f.readline()) - 1
    nums = list(map(int, f.readline().split(" ")))
    for i in range(1, n + 1):
        if n % i == 0:
            answer = True
            for j in range(n // i - 1):
                if nums[i * j:i * (j + 1)] != nums[i * (j + 1):i * (j + 2)]:
                    answer = False
                    break
            if answer:
                with open("OUTPUT.TXT", "w") as f1:
                    f1.write(str(i))
                break

# TODO: test 10 fail
