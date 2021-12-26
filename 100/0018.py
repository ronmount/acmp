def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


with open("INPUT.TXT", "r") as f:
    num = int(f.readline())
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(factorial(num)))