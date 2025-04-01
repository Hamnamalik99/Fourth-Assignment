def access_element(lst, index):
    """Returns the element at a given index, handling out-of-range cases."""
    try:
        return lst[index]  # Try to access the element at the index
    except IndexError:  # Handle the IndexError if index is out of range
        return "Index out of range."


def modify_element(lst, index, new_value):
    """Modifies an element at a given index with a new value."""
    try:
        lst[index] = new_value  # Modify the element at the index
        return lst  # Return the updated list
    except IndexError:  # Handle the case when the index is out of range
        return "Index out of range."


def slice_list(lst, start, end):
    """Returns a sliced portion of the list with improved index validation."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):  # Validate indices
        return lst[start:end]  # Return the sliced portion
    else:
        return "Invalid indices."


def index_game():
    """Interactive index-based game for lists."""
    lst = [1, 2, 3, 4, 5]  # Example list

    while True:
        print("\nCurrent list:", lst)  # Display the current list
        print("Choose an operation: access, modify, slice, exit")
        operation = input("Enter operation: ").lower()  # User input for operation

        if operation == "access":
            try:
                index = int(input("Enter index to access: "))  # User input for index
                print("Result:", access_element(lst, index))  # Display result of access
            except ValueError:
                print("Invalid input. Please enter an integer.")  # Handle non-integer input

        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))  # User input for index
                new_value = input("Enter new value: ")  # User input for new value
                print("Updated List:", modify_element(lst, index, new_value))  # Display updated list
            except ValueError:
                print("Invalid input. Please enter an integer.")  # Handle non-integer input

        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))  # User input for start index
                end = int(input("Enter end index: "))  # User input for end index
                print("Sliced List:", slice_list(lst, start, end))  # Display sliced list
            except ValueError:
                print("Invalid input. Please enter integers.")  # Handle non-integer input

        elif operation == "exit":
            print("Exiting the game. Goodbye!")  # Exit message
            break  # Break the loop to exit the game

        else:
            print("Invalid operation. Please try again.")  # Handle invalid operation


if __name__ == '__main__':
    index_game()  # Start the game
