def do_a():
    print("Doing A")

    do_b()


def do_b():
    print("Doing B")

    do_c()


def do_c():
    print("Doing C")


def do_d(n):
    print(f"Doing D{n}")


def naive_factorial(n):
    if n < 1:
        return 1

    return n * naive_factorial(n - 1)


def main():
    do_a()

    for i in range(0, 5):
        do_d(i + 1)

    print(naive_factorial(6))


if __name__ == "__main__":
    main()
