# Q5. User-Defined Modules and Packages

# Import entire module
import arithmetic

# Import selected functions
from arithmetic import addition, subtraction

# Import student package
from student import display_details, calculate_result

# Arithmetic Operations
a = 20
b = 10

print("--- Arithmetic Operations ---")
print("Addition:", addition(a, b))
print("Subtraction:", subtraction(a, b))
print("Multiplication:", arithmetic.multiplication(a, b))
print("Division:", arithmetic.division(a, b))

# Student Details
print("\n--- Student Details ---")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
student_class = input("Enter class: ")

display_details(name, roll, student_class)

# Student Results
marks = [85, 90, 80]

total, average, highest = calculate_result(*marks)

print("\n--- Student Results ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest Marks:", highest)