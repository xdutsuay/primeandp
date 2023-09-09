import subprocess
import time


def estimate_primes(start_range, end_range, num_threads):
    # Measure the time taken for the parallel version
    start_time_parallel = time.time()
    subprocess.run(['python', 'parallel_prime_finder.py'], input=f"{start_range}\n{end_range}\n{num_threads}\n",
                   text=True, check=True)
    end_time_parallel = time.time()

    # Measure the time taken for the non-parallel version
    start_time_non_parallel = time.time()
    subprocess.run(['python', 'prime_finder.py'], input=f"{start_range}\n{end_range}\n", text=True, check=True)
    end_time_non_parallel = time.time()

    # Calculate time differences
    time_difference_parallel = end_time_parallel - start_time_parallel
    time_difference_non_parallel = end_time_non_parallel - start_time_non_parallel

    return time_difference_parallel, time_difference_non_parallel


# if __name__ == "__main__":
#     start_range = int(input("Enter the starting number: "))
#     end_range = int(input("Enter the ending number: "))
#     num_threads = int(input("Enter the number of parallel tasks: "))
#
#     parallel_time, non_parallel_time = estimate_primes(start_range, end_range, num_threads)
#
#     print(f"Total time taken by parallel version: {parallel_time:.2f} seconds")
#     print(f"Total time taken by non-parallel version: {non_parallel_time:.2f} seconds")
#     print(f"Time difference: {abs(parallel_time - non_parallel_time):.2f} seconds")
