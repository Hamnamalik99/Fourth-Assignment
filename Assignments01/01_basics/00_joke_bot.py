# Constants
# PROMPT stores the question that asks what the user wants.
PROMPT = "What do you want? "  # The prompt message that will be shown to the user
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"  # The joke to be told when the user asks for it
SORRY = "Sorry I only tell jokes"  # The message displayed when the user doesn't ask for a joke

# Main function where the logic is executed
def main():
    # Ask the user what they want
    user_input = input(PROMPT)  # Taking user input based on the prompt message
    
    # Check the user's response and print the appropriate message
    if user_input == "Joke":  # If the user asks for a joke
        print(JOKE)  # Print the joke
    else:  # If the user doesn't ask for a joke
        print(SORRY)  # Apologize that the bot only tells jokes

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()  # Call the main function to run the program
