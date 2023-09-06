import pickle
from tabulate import tabulate

# File path for storing results
results_file = 'results.pkl'


def load_results():
    try:
        with open(results_file, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def main():
    results = load_results()

    if not results:
        print("No results found.")
        return

    # Create a list of dictionaries for tabulation
    table_data = []
    for key, value in results.items():
        if isinstance(value, tuple) and len(value) == 2:
            (start, end, threads), (parallel_time, non_parallel_time) = key, value
            table_data.append({
                "Input Range and Threads": f"Range: {start}-{end}, Threads: {threads}",
                "Parallel Time": f"{parallel_time:.2f} seconds",
                "Non-Parallel Time": f"{non_parallel_time:.2f} seconds",
                "Time Difference": f"{abs(parallel_time - non_parallel_time):.2f} seconds"
            })
        else:
            print(f"Invalid data for key: {key}")

    if table_data:
        # Display the data in a tabulated format
        headers = "keys"
        print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
