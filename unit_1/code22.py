num = int(input("Enter an integer: "))

if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


