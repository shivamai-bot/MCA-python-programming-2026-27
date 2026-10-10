num = int(input("Enter an integer: "))

if num < 0:
    num = abs(num)

factor_count = 0

print("The factors of", num, "are:")

if num == 0:
    print("Every non-zero integer is a factor of 0.")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            factor_count = factor_count + 1

    print()
    print("Total number of factors:", factor_count)

