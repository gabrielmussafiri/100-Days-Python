student_height = input("Input a list of students height " ).split()
for n in range(0 , len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)

total_student_height = 0
average =0

#  Using the for loop 

# for student in student_height:
#     total_student_height += student
#     average= round(total_student_height / len(student_height) -1)
# print(average)

# With the sum function

tottal_student_height = sum(student_height)
print(tottal_student_height)
