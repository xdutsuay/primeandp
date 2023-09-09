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

    # Create a list of lists for tabulation
    table_data = []
    for key, value in results.items():
        if isinstance(value, tuple) and len(value) == 2:
            (start, end, threads), (parallel_time, non_parallel_time) = key, value
            table_data.append([
                start,
                end,
                threads,
                f"{max(parallel_time, non_parallel_time):.2f} seconds"
            ])
        elif isinstance(value, float):
            start, end, threads = key
            table_data.append([
                start,
                end,
                threads,
                f"{value:.2f} seconds"
            ])
        else:
            print(f"Invalid data for key: {key}")

    # Display the data in a tabulated format
    headers = ["Start Range", "End Range", "Threads", "Time"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
