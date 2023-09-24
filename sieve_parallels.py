import math
import multiprocessing
import time


def sieve_segment(start, end):
    sieve_size = end - start + 1
    sieve = [True] * sieve_size
    sqrt_end = int(math.sqrt(end))

    for i in range(2, sqrt_end + 1):
        if sieve[i - start]:
            for j in range(i * i, end + 1, i):
                sieve[j - start] = False

    primes = [start + i for i in range(sieve_size) if sieve[i]]
    return primes


def parallel_sieve(start_range, end_range, num_threads):
    step = (end_range - start_range + 1) // num_threads
    pool = multiprocessing.Pool(num_threads)
    ranges = [(start_range + i * step, start_range + (i + 1) * step - 1) for i in range(num_threads)]

    start_time = time.time()  # Record the start time

    results = pool.starmap(sieve_segment, ranges)

    end_time = time.time()  # Record the end time

    pool.close()
    pool.join()

    primes = [prime for sublist in results for prime in sublist]
    return primes, end_time - start_time


if __name__ == "__main__":
    start_range = int(input("Enter the starting number: "))
    end_range = int(input("Enter the ending number: "))
    num_threads = int(input("Enter the number of parallel tasks: "))

    primes, total_time = parallel_sieve(start_range, end_range, num_threads)

    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)
    print(f"Total time taken: {total_time:.2f} seconds")
