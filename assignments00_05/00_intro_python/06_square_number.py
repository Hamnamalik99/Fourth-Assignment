# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0

def main():
    # Ask the user to input a number
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number ** 2
    
    # Print the result
    print(f"{number} squared is {square}")

# Call the main function to execute the program
if __name__ == '__main__':
    main()


# Program user se ek number lene ke liye input() function ka use karta hai.
# Hum user ki input ko float() ke zariye floating-point number (decimal numbers) mein convert karte hain, 
# taki agar user koi decimal number daale toh woh sahi se handle ho sake.
# Hum number ko square karte hain, yaani usko apne aap se multiply karte hain.
# Output ko print karte waqt hum f-string ka use karte hain, jo user ko yeh dikhata hai ke diya gaya number 
# aur uska square kya hai.


