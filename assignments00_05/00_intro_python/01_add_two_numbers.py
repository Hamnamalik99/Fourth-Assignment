# Write a Python program that takes two integer inputs from the user and calculates their sum. 
# The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.



def main():
    # Prompt the user to enter the first number
    num1 = int(input("Enter the first number: "))
    
    # Prompt the user to enter the second number
    num2 = int(input("Enter the second number: "))
    
    # Calculate the sum of the two numbers
    total_sum = num1 + num2
    
    # Print the result with an appropriate message
    print(f"The total sum is: {total_sum}")

# This line is required to call the main function when the script is executed
if __name__ == '__main__':  
     main()


# yeh use aapko yeh ensure karne mein madad karta hai ki aapka main() function sirf tab run ho jab aap script 
# ko direct execute karein. agar ap script ko import karo gay toh main funcation nahi chaly ga.
    
