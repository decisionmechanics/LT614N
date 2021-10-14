import sys
import time
import primes


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


if __name__ == "__main__":
    n = int(sys.argv[1])

    start_time = time.perf_counter()

    prime = primes.find_nth_prime(n)

    duration = time.perf_counter() - start_time

    print(
        f"Calculated {n}{get_number_suffix(n)} prime to be {prime} in {duration:.2f} second(s)"
    )
