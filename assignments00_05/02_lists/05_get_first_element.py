# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first
# element in the list. The list is guaranteed to be non-empty.


# Function jo list ke pehle element ko print karega
def get_first_element(lst):
    # List ke pehle element ko print karna (lst[0) se hum pehla element access karte hain)
    print(lst[0])  

# Function jo user se list input lega
def get_lst():
    # Ek khaali list banayi gayi hai
    lst = []
    
    # Pehla element input lene ke liye user se request kar rahe hain
    elem = input("Please enter an element of the list or press enter to stop: ")
    
    # Yeh loop tab tak chalega jab tak user kuch input de
    while elem != "":  # Jab tak user kuch input nahi dega, tab tak loop chalega
        lst.append(elem)  # Input ko list mein add karte hain
        # User se agla element input lene ki request
        elem = input("Please enter an element of the list or press enter to stop: ")
    
    # Jab user empty input de deta hai, tab list return ki jaati hai
    return lst

# Main function jo puri program ko run karega
def main():
    # User se list lene ke liye get_lst function ko call kar rahe hain
    lst = get_lst()  # Get user-inputted list
    
    # Ab us list ke pehle element ko print karne ke liye get_first_element function ko call karte hain
    get_first_element(lst)  # Print first element

# Yeh ensure karta hai ke agar script directly run ho rahi ho toh main function call ho
if __name__ == '__main__':
    main()  # Program ko execute karte hain
