import random  # Yeh module random number ya characters generate karne ke liye use hota hai.
import string  # Yeh module letters, digits, aur punctuation symbols provide karta hai.

print("\n🔒 Welcome to Project 7: Password Generator! 🛡️")  # Game ka welcome message print ho raha hai.

# Password generation function
def generate_password(length):
    # Characters ka set bana rahe hain jisme letters (uppercase, lowercase), digits, aur punctuation symbols hain.
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Yeh line password generate karne ke liye hai. Randomly characters ko select kar ke password banaya jaata hai.
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password  # Password return karte hain.

try:
    # User se input le rahe hain ki woh kitne passwords generate karna chahta hai.
    num_passwords = int(input("How many passwords do you want to generate? "))  
    
    # User se input le rahe hain ki har password ka length kitna hona chahiye.
    password_length = int(input("Enter password length: "))  
    
    print("\nHere are your secure passwords:")  # Passwords display karne ka message.

    # Loop chalega jitni passwords generate karni hain.
    for _ in range(num_passwords):
        # Har iteration mein ek new random password generate ho raha hai.
        print(generate_password(password_length))  # Generated password ko print karte hain.
    
    print("🎉 Passwords generated successfully! 🔐")  # Password generation ka success message.

except ValueError:
    # Agar user ne invalid input diya (jaise text ya non-integer value), to yeh error message show hoga.
    print("Please enter valid numbers!")  
