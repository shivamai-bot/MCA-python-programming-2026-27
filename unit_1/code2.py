basic_salary = int(input("Enter basic salary "))

da = (basic_salary / 100) * 40
hra = (basic_salary / 100) * 20
gross = (basic_salary + da + hra)
tax = (gross / 100) * 18
net = (gross - tax)

print("-----------------------------------")
print("Your Dearence allownce is :", da)
print("Your housing allownce is :", hra)
print("Your gross salary is :", gross)
print("Your applicaple tax is :", tax)
print("-----------------------------------")
print("Your Net salary is :", net)

