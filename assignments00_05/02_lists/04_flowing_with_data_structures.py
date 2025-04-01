# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):
# Enter a message to copy: Hello world!

# List before: []
# List after: ['Hello world!', 'Hello world!', 'Hello world!']

# (Note. The concept of immutable/mutable data types is called mutability. Be careful because different
#  programming languages have different rules regarding mutability!)






# Function to add three copies of 'data' to the list 'data_list' data_list aur data ko arguments ke tor par leta hai.
def add_three_copies(data_list, data):
    # 'data' ko 'data_list' mein pehli baar add kiya jaa raha hai 
    # append it is used to add a single item to the end of the list.
    data_list.append(data)
    
    # 'data' ko 'data_list' mein doosri baar add kiya jaa raha hai
    data_list.append(data)
    
    # 'data' ko 'data_list' mein teesri baar add kiya jaa raha hai
    data_list.append(data)

# Main function jo program ko run karega
def main():
    # User se message input karne ko kaha gaya hai
    message = input("Enter a message to copy: ")

    # Ek khaali list banayi gayi hai jisme hum message ko store kar rahy hain.
    my_list = []

    # List ko modify karne se pehle, uski current state ko print kiya jaa raha hai (jo ke abhi khaali hai)
    print(f"List before: {my_list}")
    
    # 'add_three_copies' function ko call kiya gaya hai jo message ko 3 dafa list mein add karega
    add_three_copies(my_list, message)

    # List ko modify karne ke baad, jo function ke execute hone ke baad modify ho gayi hai.
    print(f"List after: {my_list}")

# Yeh check karta hai ke agar script ko directly run kiya gaya hai ya nahi (import kiya gaya hai ya nahi)
if __name__ == "__main__":  
    # Main function ko call kiya gaya hai taake program run ho
    main()
