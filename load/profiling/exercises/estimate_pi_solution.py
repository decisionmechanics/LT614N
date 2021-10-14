from random import random
import sys


def generate_random_point():
    x = random() * 2.0 - 1.0
    y = random() * 2.0 - 1.0

    return x, y


def is_inside_circle(x, y):
    return x * x + y * y <= 1.0


def calculate_pi(number_of_samples, number_of_samples_inside_circle):
    return (number_of_samples_inside_circle / number_of_samples) * 4


def estimate_pi(number_of_samples: int) -> float:
    number_of_samples_inside_circle = 0

    for _ in range(number_of_samples):
        x, y = generate_random_point()

        if is_inside_circle(x, y):
            number_of_samples_inside_circle += 1

    return calculate_pi(number_of_samples, number_of_samples_inside_circle)


def main():
    number_of_samples = 1_000_000

    if len(sys.argv) > 1:
        number_of_samples = int(sys.argv[1])

    pi = estimate_pi(number_of_samples)

    print(f"PI is esimated to be {pi:.4f} (using {number_of_samples} sample(s))")


if __name__ == "__main__":
    main()
