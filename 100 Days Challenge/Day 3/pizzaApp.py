print("Welcome to Pizza Deliveries")
size = input("What size do you want ? S,M, or L")
add_pepperoni = input(" Do you want pepperoni? Y or N")
extra_cheese = input ("Do you want extra cheese? Y or N")
bill =0

if size == "S" :
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
        if add_pepperoni == "N":
            bill-=2
        if extra_cheese == "Y":
            bill += 1
        if extra_cheese == "N":
            bill -= 1
       
    print(f" Your Final bill is R{bill}")
    
elif size == "M" :
   bill = 20
   if add_pepperoni == "Y":
        bill += 3
        if add_pepperoni == "N":
            bill 
        if extra_cheese == "Y":
            bill += 1
        if extra_cheese == "N":
            bill 
        print(f" Your Final bill is R{bill}")
elif size == "L" :
    bill =25
    if add_pepperoni == "Y":
        bill += 3
        if add_pepperoni == "N":
            bill 
        if extra_cheese == "Y":
            bill += 1
        if extra_cheese == "N":
            bill 
        print(f" Your Final bill is R{bill}")
else :
    print(" Incorrect size , please select S,M, or L")