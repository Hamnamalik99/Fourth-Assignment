import time  # Yeh line "time" module ko import kar rahi hai, jisse hum time ke related functions use kar sakte hain, jaise sleep.

print("⏳ Welcome to Project 6: Countdown Timer! ⏰")  # Yeh line ek welcome message print kar rahi hai jo countdown timer ke baare mein hai.

try:
    seconds = int(input("Enter countdown time in seconds: "))  # Yeh line user se countdown time (seconds mein) input lene ke liye hai, aur usko integer mein convert kar rahi hai.
except ValueError:  # Agar user ne koi number ke alawa kuch enter kiya (jaise text), to yeh error handle kar rahi hai.
    print("Invalid input! Please enter a number.")  # Agar input valid number nahi tha, to yeh error message print kar rahi hai.
    exit()  # Agar input galat ho, to program ko yahan se exit kar diya jaata hai.

while seconds > 0:  # Yeh loop tab tak chalega jab tak seconds 0 se zyada hain.
    mins, secs = divmod(seconds, 60)  # "divmod" function seconds ko minutes aur seconds mein divide karta hai.
    timer = f'{mins:02}:{secs:02}'  # Yeh line minutes aur seconds ko "MM:SS" format mein dikhane ke liye banayi gayi hai.
    print(timer, end='\r')  # Yeh line har second mein timer ko update kar rahi hai. "end='\r'" ka matlab hai ke purani value ko overwrite karna.
    time.sleep(1)  # Yeh line ek second ka wait kar rahi hai, taake timer ko 1 second ke liye rukke update kiya jaaye.
    seconds -= 1  # Yeh line seconds ko ek kam kar rahi hai har iteration mein, taake countdown chal sake.

print("🎉 Time's up! Countdown completed successfully! 🎊")  # Jab countdown khatam ho jaata hai, to yeh message print hota hai jo batata hai ke time up ho gaya hai.
