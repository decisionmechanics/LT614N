import math
import sys


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def get_number_suffix(n):
    if 11 <= n <= 13:
        return "th"
    elif n % 10 == 1:
        return "st"
    elif n % 10 == 2:
        return "nd"
    elif n % 10 == 3:
        return "rd"
    else:
        return "th"


def main():
    n = int(sys.argv[1])
    count = n

    candidate = 1

    while count > 0:
        candidate += 1

        if is_prime(candidate):
            count -= 1

    print(f"The {n}{get_number_suffix(n)} prime is {candidate}")


if __name__ == "__main__":
    main()
