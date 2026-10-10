maths = float(input("Enter marks obtained in Mathematics: "))
physics = float(input("Enter marks obtained in Physics: "))
chemistry = float(input("Enter marks obtained in Chemistry: "))

total_marks = maths + physics + chemistry
overall_percentage = (total_marks / 300) * 100

if maths >= 65 and physics >= 60 and chemistry >= 60:
    if overall_percentage >= 70:
        print("Congratulations! You are eligible for admission.")
    else:
        print("Admission Denied: Overall percentage is less than 70%.")
else:
    print("Admission Denied: Minimum subject-wise marks criteria not met.")

print("Your overall percentage is:", round(overall_percentage, 2), "%")
