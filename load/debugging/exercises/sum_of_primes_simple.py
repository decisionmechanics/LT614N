import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def sum_of_primes(maximum):
    total = 0

    for i in range(2, maximum + 1):
        if not is_prime(i):
            continue

        total += i

    return total


def main():
    print(sum_of_primes(10))


if __name__ == "__main__":
    main()
