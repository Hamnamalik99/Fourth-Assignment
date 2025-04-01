# Write a program which continuously asks the user to enter values which are added one by one into a list.
# When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']



# List ko print karne ke liye function
def get_list():

    # Ek khaali list banayi gayi hai jisme user ke values store ki jaayengi
    lst = []

    # User se value input lene ka prompt
    value = input("Enter a value:")

    # Jab tak user kuch type karega, loop chalega
    while value:
        lst.append(value)  # User ke input ko list mein add karte hain.append() method ka use karke user ke input (val) ko list lst mein add kiya jaata hai.
        value = input("Enter a value:")  # Agla value input lene ke liye prompt

    # Jab user bina koi input diye Enter press karega, list ko print karenge
    print("Here's the list:", lst)

# Yeh ensure karta hai ke agar script ko directly run kiya jaaye, toh function execute ho
if __name__ == '__main__':
    get_list()  # get_list function ko call karte hain
