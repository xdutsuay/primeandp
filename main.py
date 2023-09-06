import subprocess
import time
import pickle

# File path for storing results
results_file = 'results.pkl'

def load_results():
    try:
        with open(results_file, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def save_results(results):
    with open(results_file, 'wb') as file:
        pickle.dump(results, file)

def main():
    results = load_results()

    start_range = int(input("Enter the starting number: "))
    end_range = int(input("Enter the ending number: "))
    num_threads = int(input("Enter the number of parallel tasks: "))

    key = (start_range, end_range, num_threads)

    if key in results:
        estimated_time = results[key]
        print(f"Estimated time based on similar input: {estimated_time:.2f} seconds")
    else:
        # Measure the time taken for the parallel version
        start_time_parallel = time.time()
        subprocess.run(['python', 'parallel_prime_finder.py'], input=f"{start_range}\n{end_range}\n{num_threads}\n", text=True, check=True)
        end_time_parallel = time.time()

        # Measure the time taken for the non-parallel version
        start_time_non_parallel = time.time()
        subprocess.run(['python', 'prime_finder.py'], input=f"{start_range}\n{end_range}\n", text=True, check=True)
        end_time_non_parallel = time.time()

        # Calculate time differences
        time_difference_parallel = end_time_parallel - start_time_parallel
        time_difference_non_parallel = end_time_non_parallel - start_time_non_parallel

        # Store the result for future use
        results[key] = max(time_difference_parallel, time_difference_non_parallel)

        # Save updated results to the file
        save_results(results)

        print(f"Total time taken: {results[key]:.2f} seconds")
        print(f"Time taken by parallel version: {time_difference_parallel:.2f} seconds")
        print(f"Time taken by non-parallel version: {time_difference_non_parallel:.2f} seconds")
        print(f"Time difference: {abs(time_difference_parallel - time_difference_non_parallel):.2f} seconds")

if __name__ == "__main__":
    main()
