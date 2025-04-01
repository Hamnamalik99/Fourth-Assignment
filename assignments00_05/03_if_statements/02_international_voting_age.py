# Define voting ages for each country
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48
# main() function define kiya hai jisme hum user se umar poochenge aur fir voting eligibility check karenge.
def main():
# user se unki umar poochti hai aur input() se jo value milti hai usay integer (int()) mein convert kar ke user_age variable mein store karti hai.
    user_age = int(input("How old are you? "))

    # Check if the user can vote in each country
    # agar user ki age PETURKSBOUIPO kay barabar yah zaydha hay toh if print ho ga
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")

    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

if __name__ == '__main__':
    main()