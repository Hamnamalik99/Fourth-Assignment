# Define a function to double the input number
def double():
    # Prompt the user to enter a number
    user_input = int(input("Enter a number: "))  # Convert the input to an integer

    # Calculate double of the input number
    user_inputs = user_input * 2

    # Print the result in a formatted string
    print(f"{user_input} double is {user_inputs}")  # Display the doubled value

# Ensure the function is called only when the script is run directly
if __name__ == "__main__":
    double()  # Call the double function to execute the program
