import random
from multiprocessing import Pool, cpu_count

# Precompute the list of choices outside the function
choices = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

# Function to generate a single code
def generate_code(_):
    return "".join(random.choices(choices, k=15))

# Function to generate codes in parallel and write in batches
def generate_and_write_codes(amount, batch_size=420000):
    with Pool(cpu_count()) as pool, open("amazon_codes.txt", "w") as file:
        for i in range(0, amount, batch_size):
            # Generate a batch of codes
            batch = pool.map(generate_code, range(min(batch_size, amount - i)))
            
            # Write the batch to the file
            file.write("\n".join(f"{i + j + 1}: {code}" for j, code in enumerate(batch)) + "\n")
            
            # Print progress
            print(f"Generated and wrote {i + len(batch)} codes so far...")

def main():
    # Get the number of codes from the user
    amount_of_codes = get_integer_input("Amount Of Codes: ")
    
    # Generate and write codes in parallel
    generate_and_write_codes(amount_of_codes)

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()