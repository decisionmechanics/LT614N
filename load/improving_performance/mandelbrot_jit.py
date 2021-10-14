# Adapted from:
# https://gist.githubusercontent.com/alejandrods/c0047572f6854b34a7c979ac3ddca3cb/raw/ac7a1e6b7014cba51a2ed52fbcfadaa5aafc8716/mandelbrot.py

import matplotlib.pyplot as plt
from matplotlib.pylab import imshow
from numba import jit
import numpy as np
import time


@jit(nopython=True)
def is_mandelbrot_candidate(x, y, max_iterations):
    i = 0
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iterations):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return 255


@jit(nopython=True)
def create_fractal(min_x, max_x, min_y, max_y, image, iterations):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = is_mandelbrot_candidate(real, imag, iterations)
            image[y, x] = color

    return image


def main():
    image = np.zeros((500 * 2, 750 * 2), dtype=np.uint8)
    fractal = create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)

    start_time = time.perf_counter()
    create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)
    duration = time.perf_counter() - start_time
    print(f"2nd call to create_fractal executed in {duration:.2f} second(s)")

    imshow(fractal)
    plt.savefig("mandelbrot.png")


if __name__ == "__main__":
    main()
