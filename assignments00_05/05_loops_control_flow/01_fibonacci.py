# Set the maximum value for the Fibonacci term
MAX_TERM_VALUE : int = 10000

# Main function to generate and print Fibonacci numbers
def main():
    # Initialize the first two terms of the Fibonacci sequence
    curr_term = 0  # The 0th Fibonacci number
    next_term = 1  # The 1st Fibonacci number
    
    # Loop until the current Fibonacci number exceeds the maximum term value
    while curr_term <= MAX_TERM_VALUE:
        # Print the current Fibonacci number
        print(curr_term)
        
        # Calculate the next Fibonacci number
        term_after_next = curr_term + next_term
        
        # Update the current and next terms for the next iteration
        curr_term = next_term
        next_term = term_after_next

# If this script is run directly, execute the main function
if __name__ == '__main__':
    main()
