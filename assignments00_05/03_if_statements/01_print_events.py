# Write a program that prints the first 20 even numbers. There are several correct approaches, 
# but they all use a loop of some sort. Do no write twenty print statements
# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


def main():
    # Yeh ek loop hai jo 20 dafa chalega. i ek variable
    for i in range(20):  # iska ka matlab hai 0 se le kar 19 tak 20 numbers ko loop ke andar use karna.

        print(i * 2)  # Har iteration mein, hum i ko 2 se multiply kar rahe hain taake humhe even numbers mily

if __name__ == "__main__":  # Check if the script is being run directly (not imported as a module)
    main()  # Call the main() function to execute the code
