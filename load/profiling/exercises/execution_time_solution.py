from statistics import mean, stdev
import time
import timeit

l = list(range(100_000))
s = set(range(100_000))


def lookup_in_list(n):
    return n in l


def lookup_in_set(n):
    return n in s


def time_using_perf_counter():
    print("*** Using time.perf_counter ***")
    start = time.perf_counter()
    lookup_in_list(50_000)
    duration = time.perf_counter() - start
    print(f"Looking up list took {duration} second(s)")

    start = time.perf_counter()
    lookup_in_set(50_000)
    duration = time.perf_counter() - start
    print(f"Looking up set took {duration} second(s)")


def time_using_timeit():
    print("*** Using timeit ***")
    t = timeit.repeat(stmt=lambda: lookup_in_list(50_000), number=1)
    print(f"Looking up list took {mean(t)} second(s) (sd={stdev(t)})")

    t = timeit.repeat(stmt=lambda: lookup_in_set(50_000), number=1)
    print(f"Looking up set took {mean(t)} second(s) (sd={stdev(t)})")


def main():
    time_using_perf_counter()
    time_using_timeit()


if __name__ == "__main__":
    main()

# CLI commands
# python -m timeit --setup="import execution_time_solution" "execution_time_solution.lookup_in_list(50_000)"
# python -m timeit --setup="import execution_time_solution" "execution_time_solution.lookup_in_set(50_000)"
