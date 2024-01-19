# write a program that calculates the BMI from user's weight & height
# BMI = weight(kg)/ height^2(m2)

height = input("Entre your height in m :")
weight = input("Entre your weight in kg :")

BMI = int(weight) / float(height) ** 2

if BMI < 18.5 :
    print(f"your BMI is and you are underweight")
elif BMI > 18.5 and BMI < 25 :
        print(f"your BMI is {BMI} and you are normal weight")

elif BMI >25 and BMI < 30 :
    print(f"your BMI is {BMI} and you are overweight")
elif BMI >30 and BMI < 35 :
    print(f"your BMI is {BMI}and you are Obese")
else :
     print(f"your BMI is {BMI} and you are clinically obese")

