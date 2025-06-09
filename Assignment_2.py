# Task 1: Check if a Number is Even or Odd
num=int(input("Enter a num :"))
if (num%2==0):
    print(num,"is an even number")
else: 
    print(num,"is an odd number")
# Task 2: Sum of Integers from 1 to 50 Using a Loop
# Initialize sum
total = 0
# Loop through numbers 1 to 50
for i in range(1, 51):
    total += i
# Print the result
print("The sum of integers from 1 to 50 is:", total)

