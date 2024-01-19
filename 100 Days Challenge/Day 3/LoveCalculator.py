print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_string = name1 + name2
lowercase_combine_string = combine_string.lower()

# search letter
t = lowercase_combine_string.count('t')
r = lowercase_combine_string.count('r')
u = lowercase_combine_string.count('u')
e = lowercase_combine_string.count('e')

true =t + r + u + e

l = lowercase_combine_string.count('l')
o = lowercase_combine_string.count('o')
v = lowercase_combine_string.count('v')
e = lowercase_combine_string.count('e')

love = l + o + v + e

love_score =int(str(true) + str(love))

if love_score <10 or love_score > 90 :
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are right together")
else:
    print(f" Your score is {love_score} ")

