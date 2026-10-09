
basic_salary = int(input("Enter basic salary: "))


da = (basic_salary / 100) * 40
hra = (basic_salary / 100) * 20
gross = basic_salary + da + hra
tax = (gross / 100) * 18
net = gross - tax

print("-----------------------------------")
print("Your Dearness Allowance is :", da)
print("Your Housing Allowance is  :", hra)
print("Your Gross Salary is       :", gross)
print("Your Applicable Tax is     :", tax)
print("-----------------------------------")
print("Your Net Salary is         :", net)
