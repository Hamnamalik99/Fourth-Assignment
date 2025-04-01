#Define the function to check leap year
def leap_year():
    
# Yeh line user se unki umar ya year poochti hai. input() function se jo value milti hai, wo string hoti hai 
# is liye hum int() use karte hain taake wo string ko integer mein convert kar sakein.
    year = int(input("Please enter a year:"))
    
# Yeh check karta hai ke jo year user ne diya hai, wo 4 se divide hota hai ya nahi. 
    if year % 4 == 0:
        
# Agar saal 4 se divide ho raha hai, toh yeh check karta hai ke kya wo 100 se bhi divide hota hai.
        if year % 100 == 0:
            
# Agar saal 100 se divide ho raha hai, toh phir yeh check karta hai ke kya wo 400 se bhi divide hota hai. 
            if year % 400 == 0:
                print("That's a leap year")
                
            # (Not divisible by 400)    
            else:
                print("That's not a leap year")
                
        # (Not divisible by 100)        
        else:
            print("That's a leap year")   
    
    # (Not divisible by 4)           
    else:
        print("That's not a leap year")              
        
if __name__ == "__main__":
    leap_year()        