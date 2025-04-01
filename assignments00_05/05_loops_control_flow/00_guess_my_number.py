# Import the random module to generate a random number
import random

# Function to play the game
def main():

    # Generate a random number between 1 and 99 and assign it to 'secret_number'
    secret_number = random.randint(1, 99)

    # Print the instructions to the player about the number range
    print("I'm thinking of a number between 1 and 99.")

    # Get the player's first guess by converting the input to an integer
    guess = int(input("Enter a guess: "))

    # Loop until the player guesses the correct number
    while guess != secret_number:
        # If the guess is too low, inform the player
        if guess < secret_number:
            print("Your guess is too low.")
        # If the guess is too high, inform the player
        else:
            print("Your guess is too high.")

        # Prompt the player for another guess
        print()
        guess = int(input("Enter a new guess: "))

    # Once the correct guess is made, print a congratulatory message
    print(f"Congratulations! The number was {secret_number}.")

# The entry point of the program, calling the 'main' function if the script is run directly
if __name__ == "__main__":
    main()
