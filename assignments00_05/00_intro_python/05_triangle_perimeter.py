# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter 
# of the triangle (the sum of all of the side lengths).
# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

def main():
    # Prompt the user to enter the lengths of the sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculate the perimeter of the triangle.Triangle ka perimeter calculate karne ka formula 
    perimeter = side1 + side2 + side3
    
    # Print the perimeter
    print(f"The perimeter of the triangle is {perimeter}")

# Call the main function to execute the program
if __name__ == '__main__':
    main()


# input() ka use karte hain taake user se triangle ke har side ki length pooch sakein.

# User se jo input milega, usse hum float() mein convert karenge, taki agar user decimal value de woh bhi theek handle ho sake.
