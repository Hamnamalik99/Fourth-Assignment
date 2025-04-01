
# Speed of light in meters per second
C: int = 299792458  # Yahan par speed of light ko constant value '299792458' meters per second assign kiya gaya hai.

# Function to calculate the energy of a mass
def calculate_energy():  # Yeh ek function hai jo energy calculate karega
    
    # Prompt the user to enter the mass in kilograms
    mass_in_kg: float = float(input("Enter the mass in kilograms: "))  # User se mass in kilograms input liya ja raha hai

    # Calculate the energy in joules using Einstein's formula E = m * C^2
    energy_in_joules: float = mass_in_kg * (C**2)  # Mass aur speed of light ki value se energy calculate ki ja rahi hai

    # Print the formula
    print("e = m * C^2...")  # Formula ko print kiya ja raha hai
    
    # Print the mass in kilograms
    print(f"m = {mass_in_kg} kg")  # User ka diya hua mass print kiya ja raha hai

    # Print the speed of light in meters per second
    print(f"C = {C} m/s")  # Speed of light ki value print ho rahi hai

    # Print the energy in joules
    print(f"{energy_in_joules} joules of energy!")  # Calculate ki hui energy ko joules mein print kiya ja raha hai



# Main program execution
if __name__ == "__main__":  # Yeh check karta hai agar yeh script direct run ho rahi ho
    calculate_energy()  # Agar script directly run ho rahi hai, toh calculate_energy function ko call kiya jata hai
