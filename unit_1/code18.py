num = int(input("Enter an integer: "))

if num < 0:
    temp = abs(num)
else:
    temp = num

digit_sum = 0
digit_product = 1

if temp == 0:
    digit_product = 0

while temp > 0:
    digit = temp % 10
    digit_sum = digit_sum + digit
    digit_product = digit_product * digit
    temp = temp // 10

print("Sum of digits:", digit_sum)
print("Product of digits:", digit_product)

