import math


cdef int is_prime(int n):
    cdef int i

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


cpdef int find_nth_prime(int n):
    cdef int count = n

    cdef int candidate = 1

    while count > 0:
        candidate += 1

        if is_prime(candidate):
            count -= 1

    return candidate