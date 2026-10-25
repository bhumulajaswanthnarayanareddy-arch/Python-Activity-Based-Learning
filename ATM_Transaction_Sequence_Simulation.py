


balance = float(input("Enter opening balance: Rs. "))
n = int(input("Enter number of transactions: "))

withdrawal_limit = 10000
total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

if balance < 0 or n < 0:
    print("Invalid opening balance or transaction count.")
else:
    for i in range(n):
        print("\nTransaction", i + 1)
        kind = input("Enter deposit or withdraw: ").lower()
        amount = float(input("Enter amount: Rs. "))

        if amount <= 0:
            print("Rejected: Amount must be positive.")
            rejected += 1

        elif kind == "deposit":
            balance += amount
            total_deposits += amount
            successful += 1
            print("Deposit successful.")

        elif kind == "withdraw":
            if amount > withdrawal_limit:
                print("Rejected: Withdrawal limit exceeded.")
                rejected += 1
            elif amount > balance:
                print("Rejected: Insufficient balance.")
                rejected += 1
            else:
                balance -= amount
                total_withdrawals += amount
                successful += 1
                print("Withdrawal successful.")

        else:
            print("Rejected: Invalid transaction type.")
            rejected += 1

    print("\n--- ATM SUMMARY ---")
    print("Final Balance: Rs.", round(balance, 2))
    print("Total Deposits: Rs.", round(total_deposits, 2))
    print("Total Withdrawals: Rs.", round(total_withdrawals, 2))
    print("Successful Transactions:", successful)
    print("Rejected Transactions:", rejected)
