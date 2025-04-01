import random  # Importing random module to generate random numbers

NUM_ROUNDS = 5  # Number of rounds in the game

def main():
    print("Welcome to the High-Low Game!")  # Welcome message
    print("--------------------------------")

    score = 0  # Variable to track the user's score

    # Loop through the rounds of the game
    for round_num in range(1, NUM_ROUNDS + 1):  # Loops from 1 to NUM_ROUNDS (5 rounds)
        print(f"Round {round_num}")  # Print the current round number

        # Generate random numbers for the user and the computer
        user_number = random.randint(1, 100)  # User's random number
        computer_number = random.randint(1, 100)  # Computer's random number

        print(f"Your number is {user_number}")  # Display the user's number

        # Get user input and validate it
        while True:
            # Ask the user whether they think their number is higher or lower
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            
            # Validate the input to ensure it's either 'higher' or 'lower'
            if guess in ["higher", "lower"]:
                break  # Exit the loop if the input is valid
            print("Please enter either 'higher' or 'lower'.")  # Ask again if invalid input

        # Check if the user's guess was correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increase score if the guess was correct
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")  # Print the updated score after each round

    # Display the final message based on the user's score after all rounds
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")  # If the user guessed correctly every round
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")  # If the user got at least half correct
    else:
        print("Better luck next time!")  # If the user got less than half correct

# This ensures the main function is called when the script is executed
if __name__ == '__main__':
    main()  # Run the game when the script is executed
