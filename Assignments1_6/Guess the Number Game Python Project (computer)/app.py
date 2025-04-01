import random  # Yeh line random module ko import kar rahi hai, jo randomly numbers generate karne mein kaam aata hai.

print("🎯 Welcome to Project 2: Guess the Number Game! 🤖")  # Game ka welcome message print kar rahi hai, emojis ke saath.

print("I'm thinking of a number between 1 and 5... Can you read my mind? 🧠")  # Player ko hint diya ja raha hai ke woh 1 se 5 ke beech koi number guess karein.

print("Let the battle of wits begin! 💥")  # Game shuru karne ka excitement dikhane wala message.

secret_number = random.randint(1, 5)  # Yeh line random number generate kar rahi hai jo player ko guess karna hai, aur woh number 1 se 5 ke beech hai.
guess_count = 0  # Yeh counter hai, jo guess ki ginti rakhta hai.

messages = [  # Yeh ek list hai jisme different messages hain jo guess ke result ke baad dikhaye jayenge.
    "You're getting warmer! 🔥",
    "Oops, colder... ❄️",
    "I can feel the suspense! 😱",
    "Are you a psychic? 🧙‍♀️",
    "Hmm... getting interesting! 🤔"
]

while True:  # Yeh loop tab tak chalega jab tak player sahi number guess nahi kar leta.
    try:
        guess = int(input("Enter your guess (1-5): "))  # Yeh line player se guess lene ke liye hai, aur usko integer mein convert karne ke liye try kiya gaya hai.
        if guess < 1 or guess > 5:  # Agar guess range ke bahar hai (1 se 5 ke beech nahi), to ek error message dikhaya jaayega.
            print("Out of bounds! Please guess a number between 1 and 5. 🚫")  # Range ke bahar input diya gaya hai, isliye warning di ja rahi hai.
            continue  # Agar input galat hai, to program dobara se guess lene ke liye continue karega.
    except ValueError:  # Agar player ne koi number ke alawa kuch enter kiya (jaise text), to yeh error handle kar raha hai.
        print("Invalid input! Please enter a number. 🚨")  # Invalid input ka message dikhaya jaa raha hai.
        continue  # Agar input galat tha, to dobara guess lene ka process chalega.

    guess_count += 1  # Guess counter ko ek se badhaya ja raha hai har attempt par.

    if guess < secret_number:  # Agar guess secret number se chhota hai, to message dikhaya jaayega ki guess low hai.
        print(f"Too low! 📉 {random.choice(messages)}")  # Random feedback message diye ja rahe hain, jaise "warmer" ya "colder".
    elif guess > secret_number:  # Agar guess secret number se zyada hai, to message dikhaya jaayega ki guess high hai.
        print(f"Too high! 📈 {random.choice(messages)}")  # Yahan bhi random feedback diya jaa raha hai.
    else:  # Agar guess sahi hai, to yeh block execute hoga.
        print(f"🎉 Woohoo! You guessed the number {secret_number} in {guess_count} attempts! 🏆")  # Player ne sahi guess kiya hai, to celebrate karte hue message dikhaya jaa raha hai.
        if guess_count <= 5:  # Agar guess 5 ya usse kam attempts mein kiya gaya hai, to player ko genius bola jaa raha hai.
            print("You're a genius! 🧠")
        elif guess_count <= 10:  # Agar guess 10 attempts tak kiya gaya hai, to great job ka message diya jaa raha hai.
            print("Great job! That was impressive! ⭐")
        else:  # Agar 10 se zyada attempts lage hain, to persistence ka message diya jaa raha hai.
            print("You did it! Persistence always wins! 💪")
        break  # Jab sahi guess mil jaata hai, to loop break kar diya jaata hai.

print("Thanks for playing! You're a true mind-reader... or just lucky! 🍀")  # Game ke end par thank you ka message aur thoda mazaak.
