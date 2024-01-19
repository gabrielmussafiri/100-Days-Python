first_number = int(input("Enter the number : "))
second_number = int(input("Enter the number : "))
result = first_number/second_number
modulo = first_number % second_number
if modulo == 0:
    print(f"The first number {first_number} divid by {second_number} = : {result} , remainder is : {modulo},EVEN")
else :
    print(f"The first number {first_number} divid by {second_number} = : {result} , remainder is : {modulo} , ODD")