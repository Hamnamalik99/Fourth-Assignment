
# """
# Program: dicesimulator
# ----------------------
# Simulate rolling two dice, three times.  Prints
# the results of each die roll.  This program is used
# to show how variable scope works.
# """


import random  # random module ko import kar rahe hain taake hum random numbers generate kar sakein

def roll_dice():  # roll_dice naam ka ek function define kar rahe hain jo dice roll karega
    
    # Local variables within the function
    die1 = random.randint(1, 6)  # die1 ko 1 se 6 ke beech random number assign kar rahe hain (yeh die ka pehla face hoga)
    die2 = random.randint(1, 6)  # die2 ko bhi 1 se 6 ke beech random number assign kar rahe hain (yeh die ka doosra face hoga)
    return die1, die2  # function se die1 aur die2 ko return kar rahe hain taake unhe use kiya ja sake baad mein

# Outside the function, we store the results

for roll_number in range(1, 4):  # yeh loop 3 baar chalega (roll_number 1 se 3 tak)
    die1, die2 = roll_dice()  # roll_dice function ko call kar rahe hain aur uske results ko die1 aur die2 mein store kar rahe hain
    print(f"Roll {roll_number}: Die 1 = {die1}, Die 2 = {die2}")  
    # har roll ka result print kar rahe hain, die1 aur die2 ki values show kar rahe hain
    # random.randint() ek function hai jo ek random integer (poora number) generate karta hai.