def main():
    # Countdown from 10 to 1
    # i will take the value of the current number in the countdown.yeh ek variable hay joh for loop kay liye use hwa
    for i in range(10, 0, -1):  # Start at 10, end at 1, decrement by 1
        print(i, end=" ")
    
    # Print "Liftoff!" after the countdown
    print("Liftoff!")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()