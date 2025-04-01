# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the 
# last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


# get_last_element function jo list ke aakhri element ko print karega
def get_last_element(lst):
    # List ke aakhri element ko print karna (lst[-1] se hum aakhri element access karte hain)
    # lst[-1] ka matlab hai list ka last element. Py mein -1 index se list ke aakhri element ko access kiya jaata hai.
    print(lst[-1])

# Main function jo puri program ko run karega
def main():
    # Example list ko define kiya gaya hai
    lst = [1, 2, 3, 4, 5]
    
    # List ka aakhri element print karne ke liye get_last_element function ko call karte hain
    get_last_element(lst)

# Program ko execute karne ke liye main function ko call karte hain
if __name__ == '__main__':
    main()
