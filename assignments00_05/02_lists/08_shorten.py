# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints 
# each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should 
# leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the '
# 'autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.



# MAX_LENGTH ko 3 set kar rahe hain
MAX_LENGTH = 3

# Function jo list ko shorten karega
def shorten(lst):
    # Jab tak list ki length MAX_LENGTH se zyada hai, hum elements ko remove karte rahenge
    while len(lst) > MAX_LENGTH:  
        last_elem = lst.pop()  # List ke end se ek element remove karte hain
        print(last_elem)  # Removed element ko print karte hain

# Function jo user se list ke elements ko input karayega
def get_lst():
    lst = []  # Ek khaali list banayi gayi hai jisme hum elements store karenge
    elem = input("Please enter an element of the list or press enter to stop: ")  # User se input lene ka prompt

    # Jab tak user kuch input deta rahe, hum values ko list mein append karte rahenge
    while elem != "":  
        lst.append(elem)  # User ka input list mein add karte hain
        elem = input("Please enter an element of the list or press enter to stop: ")  # Agla input lene ke liye prompt

    return lst  # List ko return karte hain

# Main function jisme hum get_lst function ko call karte hain aur shorten function ko use karte hain
def main():
    lst = get_lst()  # User se list lete hain
    shorten(lst)  # List ko shorten karte hain

# Agar script ko directly run kiya jaye, toh main function ko call karte hain
if __name__ == '__main__':
    main()
