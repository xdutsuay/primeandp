import argparse
import pickle
import subprocess
from estimator import estimate_primes
from tabulate import tabulate

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


def main(args=None):
    #import pdb; pdb.set_trace()
    results = load_results()

    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('--start', type=int, help='Starting number')
        parser.add_argument('--end', type=int, help='Ending number')
        parser.add_argument('--threads', type=int, help='Number of parallel tasks')
        args = parser.parse_args()

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
            #results[key] = max(parallel_time, non_parallel_time)
            results[key] = (parallel_time, non_parallel_time)

            # Save updated results to the file
            save_results(results)


            print(f"\nResults for {start_range} to {end_range} with {num_threads} threads:")

            table = [("Metric", "Parallel", "Non-Parallel"),
                     ("Total time taken (seconds)", f"{parallel_time:.2f}", f"{non_parallel_time:.2f}"),
                     ("Time difference (seconds)", f"{abs(parallel_time - non_parallel_time):.2f}", ""),
                     ]

            print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

            # Add this code to print prime numbers regardless of results
            #print(f"\nPrime numbers between {start_range} and {end_range}:")
            #subprocess.run(['python', 'prime_finder.py'], input=f"{start_range}\n{end_range}\n", text=True, check=True)

        elif choice == '2':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()

