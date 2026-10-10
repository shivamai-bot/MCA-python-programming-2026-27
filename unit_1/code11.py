age = int(input("Enter your age: "))
income = float(input("Enter your monthly income (Rs.): "))
credit_score = int(input("Enter your credit score: "))

if age >= 21 and age <= 60:
    if income >= 30000:
        if credit_score >= 750:
            print("Congratulations! You are eligible for the loan.")
        else:
            print("Loan Denied: Your credit score must be 750 or higher.")
    else:
        print("Loan Denied: Your monthly income must be at least Rs. 30,000.")
else:
    print("Loan Denied: Your age must be between 21 and 60 years.")
