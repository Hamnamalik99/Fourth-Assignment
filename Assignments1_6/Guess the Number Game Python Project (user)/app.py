import random  # Yeh line "random" module ko import kar rahi hai, jisse hum random numbers generate kar sakte hain.

print("🎯 Welcome to Project 3: Guess the Number Game (User)! 🤖")  # Game ka welcome message hai jo batata hai ki yeh game user ke number ko guess karne par hai.
print("Think of a number between 1 and 5, and I'll guess it! 🧠")  # User ko keh rahe hain ki woh 1 se 5 ke beech ek number soche, jise program guess karega.

guess_count = 0  # Yeh counter hai jo track karega ki kitni baar program ne guess kiya hai.

# Yeh loop tab tak chalega jab tak guess_count 5 se kam hai (max 5 guesses allowed hain).
while guess_count < 5:
    guess = random.randint(1, 5)  # Yeh line program ko ek random number (1 se 5 ke beech) guess karne ke liye keh rahi hai.
    print(f"🔮 Is it {guess}?")  # Program apna guess print kar raha hai.

    if guess == 27:  # Yeh line galat hai, kyunki program 1 se 5 ke beech guess kar raha hai, lekin 27 koi valid guess nahi hai.
        print("🎉 Congratulations! I guessed your number 27! 🎊")  # Agar program ka guess 27 hota, toh yeh message aata (lekin yeh kabhi nahi hoga).
        break  # Yeh line program ko exit karne ke liye keh rahi hai jab sahi guess ho jaye.
    else:  # Agar guess galat hai, toh yeh part execute hoga.
        print(random.choice([  # Yeh line ek random feedback print kar rahi hai jo har guess ke saath change hoti hai.
            "Hmm... Let me channel my inner psychic! 🔥", 
            "Not yet? I'll try again! 🎯", 
            "I sense I'm getting closer... 🤔", 
            "Your number is playing hide and seek! 🤡", 
            "This is intense! 🌟"
        ]))
        input("Press Enter to let me guess again...")  # Player ko keh rahe hain ki woh Enter press karein taake program dobara guess kare.
        guess_count += 1  # Guess count ko increment kar rahe hain (ek aur attempt ka count badha rahe hain).

if guess_count == 5:  # Agar program 5 attempts ke baad bhi sahi guess nahi kar paata, to yeh part execute hota hai.
    print("😅 Oops! I couldn't guess your number in 5 tries! Maybe you're a master of mind games! 🧠")  # Yeh line program ke failure ko mazaak ke saath dikhati hai.

print("Thanks for playing! You're a tricky one! 😄")  # Game ke end par player ko thank you ka message diya jaata hai.
