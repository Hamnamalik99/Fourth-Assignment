# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and 
# outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in 
# geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:
# BC ** 2 = AB ** 2 + AC ** 2
# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse
# (BC). You will probably find math.sqrt() to be useful.
# Here's a sample run of the program (user input is in bold italics):
# Enter the length of AB: 3
# Enter the length of AC: 4
# The length of BC (the hypotenuse) is: 5.0


import math  # Yeh math module import karti hai, jisme square root (sqrt) ka function hota hai.

# Hypotenuse (BC) ki length calculate karne ka function
def calculate_hypotenuse():
    # User se AB aur AC ke lengths input lene ke liye. float() function se input ko decimal number mein convert karta hay
    AB = float(input("Enter the length of AB: "))  # AB side ka length input leti hay
    AC = float(input("Enter the length of AC: "))  # AC side ka length input leti hay
    
    # Pythagorean theorem ka use kar ke hypotenuse (BC) ki length calculate kar rahe hain
    BC = math.sqrt(AB**2 + AC**2)  # Hypotenuse BC = sqrt(AB^2 + AC^2) AB ki value 3 ko 2bar multiply karna 9 ata
    
    # Hypotenuse (BC) ki length ko print kar rahe hain
    print(f"The length of BC (the hypotenuse) is: {BC}")

# Main program execution
if __name__ == "__main__":  # Yeh ensure karta hai ke program tabhi execute ho jab yeh directly run ho
    calculate_hypotenuse()  # calculate_hypotenuse function ko call kiya gaya hai













