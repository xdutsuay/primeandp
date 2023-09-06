import pickle
import subprocess
from estimator import estimate_primes

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

    while True:
        print("\nOptions:")
        print("1. Estimate Prime Numbers")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_range = int(input("Enter the starting number: "))
            end_range = int(input("Enter the ending number: "))
            num_threads = int(input("Enter the number of parallel tasks: "))

            key = (start_range, end_range, num_threads)

            if key in results:
                estimated_time = results[key]
                print(f"Estimated time based on similar input: {estimated_time:.2f} seconds")

            parallel_time, non_parallel_time = estimate_primes(start_range, end_range, num_threads)

            # Store the result for future use
            results[key] = max(parallel_time, non_parallel_time)

            # Save updated results to the file
            save_results(results)

            print(f"Total time taken: {results[key]:.2f} seconds")
            print(f"Time taken by parallel version: {parallel_time:.2f} seconds")
            print(f"Time taken by non-parallel version: {non_parallel_time:.2f} seconds")
            print(f"Time difference: {abs(parallel_time - non_parallel_time):.2f} seconds")

            # Add this code to print prime numbers regardless of results
            print(f"Prime numbers between {start_range} and {end_range}:")
            subprocess.run(['python', 'prime_finder.py'], input=f"{start_range}\n{end_range}\n", text=True, check=True)

        elif choice == '2':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
