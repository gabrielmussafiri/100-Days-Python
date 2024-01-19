import random
names_string = input("Give me everybody's names, seperated by a comma ")
# With random and len
# the split function puted strings into a list
names = names_string.split(", ") 
# length_names = len(names)
# length_names =random.randint(0,length_names-1)
# print(f'{names[length_names]} is going to buy the meal today')

# With  random.Choice() function

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " will pay de bill")
