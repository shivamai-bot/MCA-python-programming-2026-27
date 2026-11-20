
# Recursive function for Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Recursive function for Fibonacci Series
def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)


# Calculate Factorial
num = int(input("Enter a number for factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(num))


# Generate Fibonacci Series
terms = int(input("Enter number of Fibonacci terms: "))

if terms < 0:
    print("Number of terms cannot be negative.")
else:
    print("Fibonacci Series:")
    fibonacci(terms)