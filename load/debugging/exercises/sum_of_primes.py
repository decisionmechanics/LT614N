import math


def sum_of_primes(maximum):
    total = 0

    for i in range(2, maximum + 1):
        should_continue = False

        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                should_continue = True
                break

        if should_continue:
            continue

        total += i

    return total


def main():
    print(sum_of_primes(10))


if __name__ == "__main__":
    main()
