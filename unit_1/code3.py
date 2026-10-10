units = float(input("Enter the number of units consumed: "))

bill = 0

if units <= 100:
    bill = units * 4.5
elif units <= 300:
    bill = (100 * 4.5) + ((units - 100) * 6.0)
elif units <= 500:
    bill = (100 * 4.5) + (200 * 6.0) + ((units - 300) * 7.5)
else:
    bill = (100 * 4.5) + (200 * 6.0) + (200 * 7.5) + ((units - 500) * 9.0)

print("Your total electricity bill is: Rs.", bill)
