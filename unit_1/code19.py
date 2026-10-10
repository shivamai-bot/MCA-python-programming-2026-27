num = int(input("Enter an integer: "))

if num < 0:
    temp = abs(num)
else:
    temp = num

if temp == 0:
    count = 1
    largest = 0
    smallest = 0
else:
    count = 0
    largest = -1
    smallest = 10

while temp > 0:
    digit = temp % 10
    count = count + 1
    
    if digit > largest:
        largest = digit
        
    if digit < smallest:
        smallest = digit
        
    temp = temp // 10

print("Number of digits:", count)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
