import math
import multiprocessing
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


def parallel_prime_search(start, end, num_threads):
    step = (end - start + 1) // num_threads
    pool = multiprocessing.Pool(num_threads)
    ranges = [(start + i * step, start + (i + 1) * step - 1) for i in range(num_threads)]

    start_time = time.time()  # Record the start time

    results = pool.starmap(find_primes, ranges)

    end_time = time.time()  # Record the end time

    pool.close()
    pool.join()

    return [prime for sublist in results for prime in sublist], end_time - start_time


# if __name__ == "__main__":
#     start_range = int(input("Enter the starting number: "))
#     end_range = int(input("Enter the ending number: "))
#     num_threads = int(input("Enter the number of parallel tasks: "))
#
#     primes, total_time = parallel_prime_search(start_range, end_range, num_threads)
#
#     print(f"Prime numbers between {start_range} and {end_range}:")
#     #print(primes)
#     print(f"Total time taken: {total_time:.2f} seconds")

