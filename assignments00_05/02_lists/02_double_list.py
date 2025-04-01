# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


# Numbers ki list
numbers = [1, 2, 3, 4]

# Function jo har element ko double karega
def double_elements(numbers):
    # Yeh line ek loop start kar rahi hai jo numbers list ke har element par chalega.
    for i in range(len(numbers)):         
        numbers[i] *= 2  # Har element ko 2 se multiply karenge. i index kay element ko refer kar raha hay.

# Function ko call karenge taake elements double ho jayein
double_elements(numbers)

# Modified list ko print karenge
print(numbers)  # Output hoga [2, 4, 6, 8]
