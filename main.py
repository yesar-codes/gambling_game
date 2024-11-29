def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isDigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount is greater than 0.")
        else:
            print("Please enter a number.")
    return amount