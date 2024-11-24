import random
import time
import os

# Initialize variable 'a'
a = 0
file_path = "variable_a.txt"

# Function to update and write 'a' to a file
def update_and_store():
    global a
    random_number = random.randint(1, 10)  # Generate random number between 1 and 10
    a += random_number
    with open(file_path, "w") as file:
        file.write(str(a))  # Save updated 'a' to the file
    print(f"Added {random_number}, updated 'a' to {a}, and saved to {file_path}")

# Run the loop to update 'a' every 10 seconds
try:
    print(f"Starting the program. The value of 'a' will be updated every 10 seconds.")
    while True:
        update_and_store()
        time.sleep(10)  # Wait for 10 seconds
        full_path = os.path.abspath(file_path)
        print(f"Full path of the file: {full_path}")
except KeyboardInterrupt:
    print("\nProgram terminated.")
