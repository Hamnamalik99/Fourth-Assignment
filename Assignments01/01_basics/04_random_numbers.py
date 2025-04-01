import random  # Import the random module to generate random numbers

# Constants for the number of random numbers and the range
N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1  # Minimum value for the random number
MAX_VALUE: int = 100  # Maximum value for the random number

def main():
    """
    Generates and prints 10 random numbers in the range 1 to 100.
    """
    # Generate a list of 10 random numbers in the specified range
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Print the generated numbers as a space-separated string
# map(str, random_numbers) converts each number in the list random_numbers to a string
# " ".join(...) joins these string values with a space, creating a space-separated string of numbers.
    print(" ".join(map(str, random_numbers)))

# Ensure that the main function is called only when the script is run directly
if __name__ == '__main__':
    main()  # Execute the main function to print the random numbers
