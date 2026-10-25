


budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

expenses = []
total_spending = 0

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    currency = input("Enter currency code (USD/EUR/INR): ").upper()
    amount = float(input("Enter expense amount: "))

    
    if currency == "USD":
        rate = 83.0
    elif currency == "EUR":
        rate = 90.0
    elif currency == "INR":
        rate = 1.0
    else:
        print("Unsupported currency. Expense skipped.")
        continue

    if amount < 0:
        print("Invalid amount. Expense skipped.")
        continue

    
    converted = amount * rate
    fee = converted * 2 / 100
    final_amount = converted + fee

    expenses.append((category, currency, amount,
                     converted, fee, final_amount))

    total_spending = total_spending + final_amount


print("\n--- TRAVEL EXPENSE REPORT ---")

if len(expenses) == 0:
    print("No valid expenses entered.")
else:
    largest_category, largest_amount = expenses[0][0], expenses[0][5]

    for expense in expenses:
        category, currency, amount, converted, fee, final_amount = expense

        print("\nCategory:", category)
        print("Original Amount:", amount, currency)
        print("Converted Amount: Rs.", round(converted, 2))
        print("Conversion Fee: Rs.", round(fee, 2))
        print("Final Expense: Rs.", round(final_amount, 2))

        if final_amount > largest_amount:
            largest_amount = final_amount
            largest_category = category

    print("\nTotal Spending: Rs.", round(total_spending, 2))
    print("Travel Budget: Rs.", round(budget, 2))

    if total_spending > budget:
        print("Status: Budget Exceeded")
        print("Amount Over Budget: Rs.",
              round(total_spending - budget, 2))
    else:
        print("Status: Within Budget")
        print("Remaining Budget: Rs.",
              round(budget - total_spending, 2))

    print("Largest Expense Category:", largest_category)
    print("Largest Expense Amount: Rs.",
          round(largest_amount, 2))
