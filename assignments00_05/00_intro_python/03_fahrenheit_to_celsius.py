# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal
#  places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)


# This function prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
def convert_fahrenheit_to_celsius():

    # Prompt the user to enter a temperature in Fahrenheit.
    degrees_fahrenheit: float = float(input("Enter the temperature in Fahrenheit: "))

    # Convert the temperature to Celsius.
    degrees_celsius: float = (degrees_fahrenheit - 32.00) * (5.0 / 9.0)

    # Print the temperature in Celsius.
    print(f"Temperature: {degrees_fahrenheit}°F = {degrees_celsius}°C")


if __name__ == "__main__":
    convert_fahrenheit_to_celsius()

# input() function: Program pehle user se Fahrenheit mein temperature poochta hai. may nay float() function ka 
# use kara hay taki agar user decimal mein temperature daale, toh woh sahi tareeke se handle ho jaye.
# Conversion Formula: ab  Fahrenheit to Celsius conversion formula apply karte hain:
# Output: Temperature ko Celsius mein convert karne ke baad, ab usse 2 decimal places ke saath print kara hay.