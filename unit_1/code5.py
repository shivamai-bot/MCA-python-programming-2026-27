price1 = float(input("Enter price of product 1: "))
qty1 = int(input("Enter quantity of product 1: "))

price2 = float(input("Enter price of product 2: "))
qty2 = int(input("Enter quantity of product 2: "))

price3 = float(input("Enter price of product 3: "))
qty3 = int(input("Enter quantity of product 3: "))

subtotal = (price1 * qty1) + (price2 * qty2) + (price3 * qty3)

discount = subtotal * 0.10

amount_after_discount = subtotal - discount

gst = amount_after_discount * 0.18

final_amount = amount_after_discount + gst

print("Subtotal: Rs.", subtotal)
print("Discount (10%): Rs.", discount)
print("GST (18%): Rs.", gst)
print("Final Payable Amount: Rs.", final_amount)
