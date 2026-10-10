pin = int(input("Enter your 4-digit PIN: "))

if pin == 1234:
    balance = float(input("Enter your account balance (Rs.): "))
    withdrawal_amount = float(input("Enter the amount to withdraw (Rs.): "))

    if withdrawal_amount <= 0:
        print("Transaction Failed: Invalid withdrawal amount.")
    elif withdrawal_amount > balance:
        print("Transaction Failed: Insufficient balance.")
    else:
        balance = balance - withdrawal_amount
        print("Transaction Successful! Please collect your cash.")
        print("Remaining Balance: Rs.", balance)
else:
    print("Transaction Failed: Incorrect PIN.")
