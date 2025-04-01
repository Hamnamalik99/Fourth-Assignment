
def count_numbers():
    #  Yeh ek empty dictionary banata hai jo numbers ke count ko store karegi.
    number_count = {}
# Yeh ek infinite loop hai jo tab tak chalega jab tak user 'done' type nahi karta.
    while True:
# Yeh line user se input leti hai, jisme user number de sakta hai ya 'done' type kar sakta hai.
        user_input = input("Enter a number (or 'done' to stop): ")
        
        # Agar user 'done' type kare to loop band ho jayega
        if user_input.lower() == 'done':
            break
        
# Input ko integer mein convert karte hain
# agar input valid number nahi hota toh ValueError aata hai aur program user ko valid number dene ka kehata hai.
        try:
            number = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
# Agar number dictionary mein hai to count increment karte hain, warna number ko dictionary mein add karte hain
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1

# Yeh loop dictionary ke har number aur uske count ko print karta hai.
    for number, count in number_count.items():
        print(f"{number} appears {count} times.")

# Function ko call karte hain
count_numbers()
