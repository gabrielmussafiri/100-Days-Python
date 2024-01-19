print("Welcome  to the tip calculator")
total_price = input("What was the total bill?")
percentage = input("What was the percentage tip would you like to give? 10,12,or 15?")
peoples = input("How many people to split the bill?")
if int(percentage) == 10 :
   result = (float(total_price) / int(peoples)) * 1.10
elif int(percentage) == 12 :
   result = (float(total_price) / int(peoples)) * 1.12
elif int(percentage) == 15 :
   result = (float(total_price) / int(peoples)) * 1.15

result =round(result,2)
print(f" each persone will pay $ {result}")
