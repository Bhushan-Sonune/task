# Task 1: Create a Dictionary of Student Marks

student_name=input("Enter the student's name ")
student_mark={
    "Alice":85,
    "Bob":90,
    "Charlie":80,
    "David":70,
}

if student_name in student_mark:
    print(f"{student_name}'s marks is {student_mark[student_name]}")
else:
    print("Student not found")

# Task 2: Demonstrate List Slicing
my_list=[1,2,3,4,5,6,7,8,9,10]
print("original list:",my_list)
# Extracts the first five elements from the list.
y=my_list[:5]
# Reverses these extracted elements.
reversed_five = y[::-1]
#  Prints both the extracted list and the reversed list
print("extracted list",y)
print("reversed list:", reversed_five)


