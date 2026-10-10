data_used = float(input("Enter your monthly mobile data usage in GB: "))

bill = 0

if data_used <= 10:
    bill = 199
elif data_used <= 30:
    bill = 199 + ((data_used - 10) * 15)
elif data_used <= 50:
    bill = 199 + (20 * 15) + ((data_used - 30) * 25)
else:
    bill = 199 + (20 * 15) + (20 * 25) + ((data_used - 50) * 40)

print("Your total mobile data bill is: Rs.", bill)
