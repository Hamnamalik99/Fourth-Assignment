# Write a program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end.
# The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like 
# this (the below numbers are made up -- your solution should have the correct values!):

# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7


def main():
    # Assign ages to each person based on the clues
    # Anton is 21 years old.
    Anton: int = 21

    # Beth is 6 years older than Anton.she is 21+7 = 27
    Beth: int = 6 + Anton               

    # Chen is 20 years older than Beth. she is 27+20 = 47
    Chen: int = 20 + Beth

    # Drew is as old as Chen's age plus Anton's age. drew is 47+21 =68
    Drew: int = Chen + Anton

    # Ethan is the same age as Chen. ethan is 47 
    Ethan: int = Chen
    
    # Print the names and their respective ages, with "years old" included
    print(f"Anton is {Anton} years old")
    print(f"Beth is {Beth} years old")
    print(f"Chen is {Chen} years old")
    print(f"Drew is {Drew} years old")
    print(f"Ethan is {Ethan} years old")

# Call the main function to execute the program
if __name__ == '__main__':
    main()

