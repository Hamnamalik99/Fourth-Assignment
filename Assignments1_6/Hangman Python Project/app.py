import random  # Yeh module randomly number ya items choose karne ke liye use hota hai.

# List of words for the game
words = ['python', 'javascript', 'hangman', 'developer', 'programming', 'challenge']  # Yeh list wo words hai jo user ko guess karne hain.

# Choose a random word
word = random.choice(words)  # Is line mein random word list se select kiya jaata hai jo user ko guess karna hai.
word_letters = set(word)  # Word ki unique letters ko ek set mein daal diya gaya hai, taake har letter ki ek hi occurrence ho.
alphabet = set('abcdefghijklmnopqrstuvwxyz')  # Yeh set hai jisme saare alphabet hain jo user guess kar sakta hai.
used_letters = set()  # Yeh set track karta hai ki kaunse letters user ne guess kiye hain.

# Number of lives
lives = 6  # User ke paas total 6 lives hain.

print("🎯 Welcome to Project 5: Hangman Game! 🕹️")  # Game ka welcome message.
print("Guess the word, one letter at a time. You have 6 lives! ❤️")  # Instructions bata rahe hain ki user ko ek letter at a time guess karna hai.

# Game loop
while len(word_letters) > 0 and lives > 0:  # Yeh loop tab tak chalega jab tak word ke sare letters guess nahi ho jaate aur lives khatam nahi hoti.
    # Show current status
    print(f"\nLives left: {lives}")  # User ko kitni lives bachi hain, yeh dikhaya jaata hai.
    print("Used letters:", ' '.join(sorted(used_letters)))  # User ke dwara guess kiye gaye letters ki list print hoti hai.

    # Display word with guessed letters
    display_word = [letter if letter in used_letters else '_' for letter in word]  # Yeh line word ko display kar rahi hai, jisme guessed letters dikh rahe hain aur baki letters '_' ke form mein hain.
    print("Word: ", ' '.join(display_word))  # Word ko format karke print kiya jaata hai.

    # Get user input
    user_letter = input("Guess a letter: ").lower()  # User se ek letter guess karne ko bola jaata hai, aur usko lowercase mein convert kiya jaata hai.

    if user_letter in alphabet - used_letters:  # Agar user ka letter alphabet mein hai aur woh letter pehle guess nahi kiya gaya hai.
        used_letters.add(user_letter)  # Yeh line user ke guessed letter ko used_letters set mein add kar deti hai.
        if user_letter in word_letters:  # Agar guessed letter word mein hai, to word_letters se woh letter remove kar diya jaata hai.
            word_letters.remove(user_letter)
        else:
            lives -= 1  # Agar guessed letter wrong hai, to ek life kam kar di jaati hai.
            print("Wrong guess! ❌")  # Wrong guess hone par message dikhaya jaata hai.
    elif user_letter in used_letters:  # Agar user ne pehle hi woh letter guess kiya ho.
        print("You already guessed that letter! 🤔")  # Player ko bataya jaata hai ki woh letter already guess kar chuka hai.
    else:
        print("Invalid input. Please guess a letter. 🚨")  # Agar user ka input valid nahi hai (jaise special characters ya numbers).
        
# Win or lose
if lives == 0:  # Agar lives khatam ho gayi hain, to game over hai.
    print(f"\nGame Over! You lost. The word was '{word}'. 💀")  # Game over ka message aur sahi word bata diya jaata hai.
else:
    print(f"\nCongratulations! You guessed the word '{word}' correctly! 🎉")  # Agar user ne word sahi guess kar liya, to win message dikhaya jaata hai.

print("Thanks for playing! 🏆")  # Game ke end par thanks ka message.
