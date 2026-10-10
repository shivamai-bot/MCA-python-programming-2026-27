percentage = float(input("Enter the student's percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage! Please enter a value between 0 and 100.")
else:
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 35:
        grade = "E"
    else:
        grade = "Fail"

    print("The student's grade is:", grade)
