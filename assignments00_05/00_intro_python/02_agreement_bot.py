# Write a program which asks the user what their favorite animal is, and then always responds with 
# "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the
#  user input!):

def main():
    # Ask the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")
    
    # Respond with a message including the user's favorite animal
    print(f"My favorite animal is also {favorite_animal}!")

# Call the main function to execute the program
if __name__ == '__main__':
    main()


#  input() function: Yeh function user se input lene ke liye use hota hai.  
#  f-string: Jab hum user ka input le lete hain, toh f-string ka use karte hain.
