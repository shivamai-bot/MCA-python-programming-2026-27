num = int(input("Enter an integer: "))

if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

if num == 0:
    parity = "Neither Even nor Odd (Zero)"
elif num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

print("The number is:", sign, "and", parity)
