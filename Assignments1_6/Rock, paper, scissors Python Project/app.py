# Importing necessary libraries
import random  # Random module for selecting the computer's choice
import time    # Time module for adding delays (to make the game feel more dramatic)

# Dictionary containing choices and their emoji representations
choices = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

# Initializing scores and round count
user_score = computer_score = 0  # Both scores start at 0
rounds = 0  # Round counter starts at 0

# Welcome message
print("🎲 Welcome to Rock, Paper, Scissors: Ultimate Showdown! 🚀")
print("🔔 Type 'q' anytime to quit.\n")

# Infinite loop for the game to keep running until the user quits
while True:
    user = input("👉 Choose your move (rock/paper/scissors): ").lower()  # User input for their move
    
    # Checking if the user wants to quit
    if user == "q":
        print("\n🏆 Final Score:")
        print(f"   You: {user_score} | Computer: {computer_score}")
        print(f"   Total Rounds Played: {rounds}")
        print("👋 Thanks for playing! See you next time! 😊")
        break  # Exiting the loop and ending the game

    # Checking if the user's input is valid
    if user not in choices:
        print("⚠️ Oops! That's not a valid move. Please choose rock, paper, or scissors. 🚫\n")
        continue  # If invalid, prompt again without advancing the round

    # Increment the round counter
    rounds += 1
    print("\n⏳ Computer is making its move...")
    time.sleep(1)  # Adding a slight delay for dramatic effect
    computer = random.choice(list(choices))  # Computer chooses a random move from choices
    print(f"🤖 Computer chose: {choices[computer]} ({computer.capitalize()})")

    # Checking for a tie
    if user == computer:
        print("🤝 It's a tie! Both moves are equal.")
    
    # Checking if the user wins
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        user_score += 1  # User wins this round
        print("🎉 You win this round! Fantastic move! 🔥")
    
    # If the computer wins
    else:
        computer_score += 1
        print("😢 You lost this round. Don't worry, keep trying! 💪")

    # Displaying the current score and a separator for clarity
    print(f"📊 Current Score: You {user_score} - {computer_score} Computer")
    print("------------------------------------------------\n")
