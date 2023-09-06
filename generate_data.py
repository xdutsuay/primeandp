import subprocess
import random


# Function to generate random input
def generate_random_input():
    start_range = random.randint(1, 1000)
    end_range = random.randint(start_range, 10000)
    num_threads = random.randint(1, 10)
    return start_range, end_range, num_threads


# Loop to generate and run random inputs
for _ in range(10):  # You can adjust the number of runs as needed
    start_range, end_range, num_threads = generate_random_input()
    subprocess.run(['python', 'main.py'], input=f"{start_range}\n{end_range}\n{num_threads}\n", text=True, check=True)
