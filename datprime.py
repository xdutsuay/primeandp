import math
import time
import os
import struct

current_file = os.path.basename(__file__)

# Constants for file paths and block size
PRIMES_FILE = 'primes.dat'
INDEX_FILE = 'index.txt'
BLOCK_SIZE = 10000  # Adjust as needed

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

def write_primes_to_file(start, end):
    with open(PRIMES_FILE, 'ab') as file:
        primes = find_primes(start, end)
        for prime in primes:
            file.write(struct.pack('!Q', prime))  # Write primes as 8-byte unsigned integers

def load_primes_from_file(start, end):
    primes = []
    with open(PRIMES_FILE, 'rb') as file:
        while True:
            data = file.read(8)  # Read 8 bytes (64 bits) at a time
            if not data:
                break
            prime = struct.unpack('!Q', data)[0]
            if start <= prime <= end:
                primes.append(prime)
    return primes

def update_index(start, end):
    with open(INDEX_FILE, 'a') as file:
        file.write(f"{start}-{end}\n")

def find_primes_in_range(start_range, end_range):
    primes = []

    # Check if the range is already covered by existing blocks
    try:
        with open(INDEX_FILE, 'r') as file:
            for line in file:
                block_start, block_end = map(int, line.strip().split('-'))
                if start_range >= block_start and end_range <= block_end:
                    primes.extend(load_primes_from_file(start_range, end_range))
                    break
    except FileNotFoundError:
        print(f"'{INDEX_FILE}' not found. Creating a new index file...")

    # Calculate and store new primes if necessary
    if not primes:
        write_primes_to_file(start_range, end_range)
        update_index(start_range, end_range)
        primes.extend(load_primes_from_file(start_range, end_range))

    return primes

if __name__ == "__main__":
    start_range = int(input("Enter the starting number: "))
    end_range = int(input("Enter the ending number: "))

    start_time = time.time()  # Record the start time

    primes = find_primes_in_range(start_range, end_range)

    end_time = time.time()  # Record the end time

    print(f"Prime numbers between {start_range} and {end_range}:")
    print(current_file, primes)
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
