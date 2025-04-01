# Function that prints countdown from 10 to 1 and then outputs Liftoff!
def main():

    # Loop through the numbers from 10 to 1 (inclusive) and print them
    for n in range(10):
        # Print the number (10 - n ensures we print 10, 9, ..., 1)
        print(10 - n)

    # Print the liftoff message
    print("Liftoff!")


# The entry point of the program, calling the main function when the script is run directly
if __name__ == "__main__":
    main()
