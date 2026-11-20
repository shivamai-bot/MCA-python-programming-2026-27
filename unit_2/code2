
def student_result(name, *marks, **info):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    return total, average, highest


# Accept student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
student_class = input("Enter class: ")

n = int(input("Enter number of subjects: "))

subjects = []
marks = []

for i in range(n):
    subject = input(f"Enter subject {i+1} name: ")
    mark = float(input(f"Enter marks in {subject}: "))
    subjects.append(subject)
    marks.append(mark)

# Function call using *args and **kwargs
total, average, highest = student_result(
    name, *marks, roll_no=roll_no, student_class=student_class
)

# Display student result
print("\n--- Student Result ---")
print("Name:", name)
print("Roll Number:", roll_no)
print("Class:", student_class)

for i in range(n):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)