import math
import time


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = math.isqrt(num)
    for divisor in range(3, max_divisor + 1, 2):
        if num % divisor == 0:
            return False
    return True


def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    start_range = int(input("Enter the starting number: "))
    end_range = int(input("Enter the ending number: "))

    start_time = time.time()  # Record the start time

    primes = find_primes(start_range, end_range)

    end_time = time.time()  # Record the end time

    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
