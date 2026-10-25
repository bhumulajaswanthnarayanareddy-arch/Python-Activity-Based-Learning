


products = []
n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")
else:
    for i in range(n):
        print("\nProduct", i + 1)
        name = input("Product name: ")
        opening = int(input("Opening stock: "))
        incoming = int(input("Incoming quantity: "))
        dispatched = int(input("Dispatched quantity: "))
        closing = int(input("Recorded closing stock: "))
        minimum = int(input("Minimum required stock: "))

        if (opening < 0 or incoming < 0 or dispatched < 0
                or closing < 0 or minimum < 0):
            print("Invalid stock values. Product skipped.")
            continue

        expected = opening + incoming - dispatched

        if expected < 0:
            status = "Error: Dispatch exceeds available stock"
            discrepancy = closing - expected
        else:
            discrepancy = closing - expected

            if discrepancy == 0:
                status = "Stock Matches"
            else:
                status = "Stock Discrepancy"

        replenishment = minimum - closing

        if replenishment < 0:
            replenishment = 0

        products.append(
            (name, expected, closing, discrepancy,
             replenishment, status)
        )

    print("\n--- INVENTORY REPORT ---")

    for product in products:
        name, expected, closing, discrepancy, replenishment, status = product

        print("\nProduct:", name)
        print("Expected Closing Stock:", expected)
        print("Recorded Closing Stock:", closing)
        print("Discrepancy:", discrepancy)
        print("Status:", status)
        print("Replenishment Required:", replenishment)
