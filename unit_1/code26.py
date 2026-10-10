num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

a = num1
b = num2

while b > 0:
    remainder = a % b
    a = b
    b = remainder

gcd = a

lcm = (num1 * num2) // gcd

print("The GCD of", num1, "and", num2, "is:", gcd)
print("The LCM of", num1, "and", num2, "is:", lcm)
