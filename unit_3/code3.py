
# Create a list
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

# Insert element at specified position
value = int(input("Enter value to insert: "))
pos = int(input("Enter position: "))
numbers.insert(pos - 1, value)

print("After Insertion:", numbers)

# Remove element at specified position
pos = int(input("Enter position to remove: "))
if 1 <= pos <= len(numbers):
    numbers.pop(pos - 1)

print("After Removing:", numbers)

# Remove element by value
value = int(input("Enter value to remove: "))
if value in numbers:
    numbers.remove(value)

print("Updated List:", numbers)

# Append and Extend
numbers.append(100)
numbers.extend([200, 300])

print("After Append and Extend:", numbers)

# List Concatenation and Repetition
print("Concatenation:", numbers + [400, 500])
print("Repetition:", numbers * 2)

# Indexing and Membership
print("First Element:", numbers[0])

search = int(input("Enter number to search: "))
print("Element Present:", search in numbers)

# Maximum, Minimum and Sum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Sorting
numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)

# Reverse
numbers.reverse()
print("Reversed List:", numbers)

# List Comprehension
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
squares = [x * x for x in numbers]

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Squares:", squares)