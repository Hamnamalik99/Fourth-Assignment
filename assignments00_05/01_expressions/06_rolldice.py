# Simulate rolling two dice, and prints results of each roll as well as the total.

import random  # Importing the random module to generate random numbers

# Function to simulate rolling two dice
def roll_two_dice():
    die1 = random.randint(1, 6)  # First die roll (random number between 1 and 6)
    die2 = random.randint(1, 6)  # Second die roll (random number between 1 and 6)
    
    # Calculate the total of both dice
    total = die1 + die2
    
    # Print the results of each die roll and the total
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

# Main execution of the program
if __name__ == "__main__":
    roll_two_dice()  # Call the function to roll the dice and print the results


#  F-string Iska main purpose yeh hai ke hum variables ko direct string ke andar
# (insert) kar sakein, bina kisi complex formatting ke.