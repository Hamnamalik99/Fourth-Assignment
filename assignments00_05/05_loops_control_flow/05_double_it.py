# Main function
def main():
    
# This asks the user to input a number and converts the input to an integer.
    curr_value = int(input("Enter a number: "))

#  This loop continues as long as the value of curr_value is less than 100.
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value)  # Print the updated value

# Entry point of the program
if __name__ == '__main__':
    main()
