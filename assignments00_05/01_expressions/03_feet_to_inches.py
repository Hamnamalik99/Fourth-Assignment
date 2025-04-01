
# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Function to convert feet to inches
def convert_feet_to_inches():
    # Ask the user to input a value in feet
    feet = float(input("Enter the number of feet: "))  # Taking input from the user as float
    
    # Convert feet to inches
    inches = feet * 12  # 1 foot = 12 inches
    
    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")  # Output the result in inches

# Main program execution
if __name__ == "__main__":
    convert_feet_to_inches()  # Call the function to perform the conversion
