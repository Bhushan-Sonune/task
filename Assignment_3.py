# Task 1: Calculate Factorial Using a Function
numbers=int(input("Enter the numbers:"))
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
factorial(numbers)
print("factorial of",numbers,"is",factorial(numbers))

# Task 2: Using the Math Module for Calculations
import math
numbers=int(input("Enter the numbers:"))
sqrt = math.sqrt(numbers)
print("square root of",numbers,"is",sqrt)
logarithm=math.log(numbers)
print("logarithm of",numbers,"is",logarithm)
sine=math.sin(numbers)
print("sine of",numbers,"is",sine)