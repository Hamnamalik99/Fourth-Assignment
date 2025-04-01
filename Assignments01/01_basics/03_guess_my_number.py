import random  # Import the random module to generate random numbers

# Main function where the guessing game logic is implemented
def main():
    # Generate a random number between 1 and 99 (inclusive)
    secret_number = random.randint(1, 99)  
    print("I am thinking of a number between 1 and 99...")  # Let the player know what to guess

    # Start an infinite loop for the guessing process
    while True:
        # Get the player's guess (convert the input to an integer)
        guess = int(input("Enter a guess: "))  

        # If the guess is correct, congratulate the player and break out of the loop
        if guess == secret_number:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop once the correct guess is made

        # Provide feedback based on how close the guess is
        elif abs(secret_number - guess) <= 5:  # If the guess is within 5 of the secret number
            print("Very close!")  
        elif guess < secret_number:  # If the guess is lower than the secret number
            print("Your guess is too low.")
        else:  # If the guess is higher than the secret number
            print("Your guess is too high.")

# This ensures that the main function is called when the script is run directly
if __name__ == '__main__':
    main()  # Start the guessing game when the script is executed
