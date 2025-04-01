# Dictionary storing gravity multipliers for each planet
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def mars_weight():
    """Prompts user for Earth weight and calculates weight on Mars."""
    earth_weight = float(input("Enter a weight on Earth: "))  # Prompt for Earth's weight
    mars_weight = round(earth_weight * GRAVITY_FACTORS["Mars"], 2)  # Calculate Mars weight
    print(f"The equivalent weight on Mars: {mars_weight}")  # Display the result

def planetary_weight():
    """Prompts user for Earth weight and calculates weight on any planet."""
    earth_weight = float(input("Enter a weight on Earth: "))  # Prompt for Earth's weight
    planet = input("Enter a planet: ")  # Ask for the planet name

    # Check if the planet exists in the GRAVITY_FACTORS dictionary
    if planet in GRAVITY_FACTORS:
        # Calculate the weight on the chosen planet and round to 2 decimal places
        weight_on_planet = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"The equivalent weight on {planet}: {weight_on_planet}")  # Display the result
    else:
        # Handle invalid planet input
        print("Invalid planet name. Please enter a valid planet.")

def main():
    """Main function to allow user to choose between Mars or any planet."""
    print("Choose an option:")  # Display options to the user
    print("1. Calculate weight on Mars")
    print("2. Calculate weight on any planet")
    
    choice = input("Enter 1 or 2: ")  # User's choice
    
    if choice == "1":  # If the user chooses option 1, calculate weight on Mars
        mars_weight()
    elif choice == "2":  # If the user chooses option 2, calculate weight on any planet
        planetary_weight()
    else:  # If an invalid choice is made
        print("Invalid choice. Please enter 1 or 2.")  # Display error message

# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
