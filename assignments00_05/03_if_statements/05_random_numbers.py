
# ismay hum koi bhi  random number choose kar sakty hain
import random  

N_NUMBERS = 10  # Number of random numbers
MIN_VALUE = 1    # Minimum value 
MAX_VALUE = 100  # Maximum value 

def main():
 # Generate and print 10 random numbers between 1 and 100
# Yeh random module ka ek function hai jo do arguments (MIN_VALUE aur MAX_VALUE) ke beech ek random integer generate karta hai.
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))
# woh range hain jisme aapko random number chahiye hota hai.
# Call the main function
if __name__ == '__main__':
    main()