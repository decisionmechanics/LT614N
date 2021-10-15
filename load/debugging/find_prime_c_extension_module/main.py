import findprime


def main():
    n = int(input("Which (nth) prime do you wish to find? "))

    prime = findprime.find_nth_prime(n)

    print(f"The {n}th prime is {prime}")


if __name__ == "__main__":
    main()
