
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(a, b, operation="addition"):
    if operation == "addition":
        return add(a, b)
    elif operation == "subtraction":
        return subtract(a, b)
    elif operation == "multiplication":
        return multiply(a, b)
    elif operation == "division":
        return divide(a, b)

# Input
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Function calls
print("Addition:", calculate(x, y))
print("Subtraction:", calculate(a=x, b=y, operation="subtraction"))
print("Multiplication:", calculate(x, y, "multiplication"))

if y != 0:
    print("Division:", calculate(x, y, "division"))
else:
    print("Division is not possible.")