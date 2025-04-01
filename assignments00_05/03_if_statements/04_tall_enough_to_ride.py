# Minimum height requirement set karte hain (50 units)
MIN_HEIGHT = 50

# Function jo user se height poochti hai aur check karti hai
def check_height():
    # User se unki height poochna
    height = input("How tall are you? ")

    # Agar user ne koi height nahi di (input khaali hai)
    if height == "":
        return False  # Program ko rokna hai

    # User ki height ko integer mein convert karna
    height = int(height)

    # Check karte hain agar user ki height minimum required height se zyada hai
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")  # Agar height minimum se zyada hai
    else:
        print("You're not tall enough to ride, but maybe next year!")  # Agar height minimum se kam hai

    return True  # Iska matlab program continue kar sakta hai

# Main function jo repeatedly user se height poochti hai
def tall_enough_extension():
    while True:  # Yeh loop tab tak chalega jab tak user height nahi input karta
        if not check_height():  # Agar check_height() False return karta hai, to loop ruk jayega
            break  # Program band ho jayega agar user ne height nahi diya

# Agar script directly run ho, to tall_enough_extension() function call ho
if __name__ == "__main__":
    tall_enough_extension()
