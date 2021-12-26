def nod(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a

    return a


def main():
    with open("INPUT.TXT", "r") as f:
        a, b = map(int, f.readline().split(" "))
        with open("OUTPUT.TXT", "w") as f1:
            f1.write(f"{int(a / nod(a, b) * b)}")

main()