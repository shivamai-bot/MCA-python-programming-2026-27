n = int(input("Enter the number of students (N): "))

total_marks = 0
highest_marks = -1
lowest_marks = 101
passed_count = 0
failed_count = 0
above_75_count = 0

for i in range(1, n + 1):
    marks = float(input("Enter marks for student " + str(i) + " (out of 100): "))
    
    total_marks = total_marks + marks
    
    if marks > highest_marks:
        highest_marks = marks
        
    if marks < lowest_marks:
        lowest_marks = marks
        
    if marks >= 35:
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1
        
    if marks > 75:
        above_75_count = above_75_count + 1

class_average = total_marks / n

print("\n--- CLASS PERFORMANCE REPORT ---")
print("Class Average Marks:", round(class_average, 2))
print("Highest Marks Scored:", highest_marks)
print("Lowest Marks Scored:", lowest_marks)
print("Number of Passed Students:", passed_count)
print("Number of Failed Students:", failed_count)
print("Number of Students Scoring Above 75%:", above_75_count)
