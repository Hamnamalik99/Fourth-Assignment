
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the
#  second and also the remainder of the division.
# Here's a sample run of the program (user input is in bold italics):
# Please enter an integer to be divided: 5
# Please enter an integer to divide by: 3
#  The result of this division is 1 with a remainder of 2


# Function to divide two integers and print the result
def divide():
    # User se input lene ka message - Pehla number jo divide karna hai
    divider: int = int(input("Please enter an integer to be divided: "))  # Pehla number (dividend)

    # User se input lene ka message - Dusra number jo divide karne ke liye use hoga
    divisor: int = int(input("Please enter an integer to divide by: "))  # Dusra number (divisor)

    # Division ka result calculate karna (quotient) 10 kay andar hum 3 ko teen bar he fit kar sakty hain na
    quotient: int = divider // divisor  # Integer division se quotient calculate ho raha hai 10÷3 = 3.333

    # Division ka remainder calculate karna. EX 10 - (3 × 3) = 10 - 9 = 1. 
    remainder: int = divider % divisor  # Modulo operator se remainder calculate ho raha hai

    # Division ka result print karna
    print(f"The result of the division is {quotient} with a remainder of {remainder}.")  # Output dikhana


# Program ko execute karte waqt yeh check hota hai ke script directly run ho rahi hai
if __name__ == "__main__":
    divide()  # divide function ko call karke program execute karte hain
