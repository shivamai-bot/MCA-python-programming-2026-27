num = int(input("Enter an integer: "))

if num < 0:
    print(num, "is not an Armstrong number.")
else:
    temp = num
    count = 0
    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum = armstrong_sum + (digit ** count)
        temp = temp // 10

    if num == armstrong_sum:
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")

