start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

prime_count = 0

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        
        if is_prime:
            print(num, end=" ")
            prime_count = prime_count + 1

print()
print("Total number of prime numbers found:", prime_count)


