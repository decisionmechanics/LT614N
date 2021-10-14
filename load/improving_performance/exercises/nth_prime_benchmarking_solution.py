import math
import sys
import time


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


def find_nth_prime(n):
    count = n

    candidate = 1

    while count > 0:
        candidate += 1

        if is_prime(candidate):
            count -= 1

    return candidate


if __name__ == "__main__":
    n = int(sys.argv[1])

    start_time = time.perf_counter()

    prime = find_nth_prime(n)

    duration = time.perf_counter() - start_time

    print(
        f"Calculated {n}{get_number_suffix(n)} prime to be {prime} in {duration:.2f} second(s)"
    )
