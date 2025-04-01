# Function to print the first 20 even numbers
def even_numbers():
    # Loop through the first 20 numbers (0 to 19)
    for n in range(20):
        # Print the double of the current number (which gives the even number)
        print(n * 2)


# Entry point of the program, calling the even_numbers function
if __name__ == "__main__":
    even_numbers()
