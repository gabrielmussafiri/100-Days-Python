student_height = input("Input a list of students height " ).split()
for n in range(0 , len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)

# Without the max functions
highers_heigth = 0
for student in student_height:
    if student > highers_heigth :
        highers_heigth = student
print(f" Your higher heig is: {highers_heigth} ")
