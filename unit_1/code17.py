num = int(input("Enter an integer: "))

original_num = num
reversed_num = 0

if num < 0:
    print("Negative numbers are not palindromes.")
else:
    temp = num
    while temp > 0:
        remainder = temp % 10
        reversed_num = (reversed_num * 10) + remainder
        temp = temp // 10

    if original_num == reversed_num:
        print(original_num, "is a palindrome.")
    else:
        print(original_num, "is not a palindrome.")
