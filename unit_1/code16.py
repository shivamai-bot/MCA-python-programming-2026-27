num = int(input("Enter an integer: "))

original_num = num
reversed_num = 0

if num < 0:
    num = abs(num)

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

if original_num < 0:
    reversed_num = -reversed_num

print("The reversed number is:", reversed_num)
