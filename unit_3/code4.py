
# Create a tuple of student roll numbers
roll_numbers = (101, 102, 103, 104, 105)

print("--- Tuple Operations ---")
print("Tuple:", roll_numbers)

# Tuple Indexing and Slicing
print("First Element:", roll_numbers[0])
print("Slicing:", roll_numbers[1:4])

# Tuple Concatenation
new_tuple = roll_numbers + (106, 107)
print("Concatenation:", new_tuple)

# Create two sets
course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}

print("\n--- Set Operations ---")

# Union
print("Union:", sorted(course_a | course_b))

# Intersection
print("Intersection:", sorted(course_a & course_b))

# Difference
print("Difference:", sorted(course_a - course_b))

# Symmetric Difference
print("Symmetric Difference:", sorted(course_a ^ course_b))

# Subset and Superset
common = {103, 104}
print("Subset:", common.issubset(course_a))
print("Superset:", course_a.issuperset(common))

# Add and Remove Elements
course_a.add(107)
print("After Adding:", sorted(course_a))

course_a.remove(101)
print("After Removing:", sorted(course_a))

# Set Comprehension
squares = {x*x for x in range(1, 11) if x % 2 == 0}
print("Squares of Even Numbers:", sorted(squares))