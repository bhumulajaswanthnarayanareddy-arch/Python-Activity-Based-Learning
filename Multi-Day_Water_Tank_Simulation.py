


capacity = float(input("Enter tank capacity in litres: "))
initial = float(input("Enter initial water level in litres: "))
target = float(input("Enter target water level in litres: "))
n = int(input("Enter number of intervals: "))

if (capacity <= 0 or initial < 0 or initial > capacity
        or target < 0 or target > capacity or n <= 0):
    print("Invalid tank details.")
else:
    water = initial
    first_interval = 0
    overflow_total = 0
    shortage_total = 0

    print("\n--- WATER TANK REPORT ---")
    print("Initial water level:", water, "litres")

    if water >= target:
        first_interval = 0

    for i in range(1, n + 1):
        print("\nInterval", i)
        inflow = float(input("Enter inflow in litres: "))
        outflow = float(input("Enter outflow in litres: "))

        if inflow < 0 or outflow < 0:
            print("Invalid quantities. Interval skipped.")
            continue

        available = water + inflow

        if available > capacity:
            overflow = available - capacity
            overflow_total += overflow
            available = capacity
            print("Overflow:", overflow, "litres")
        else:
            print("Overflow: 0 litres")

        if outflow > available:
            shortage = outflow - available
            shortage_total += shortage
            water = 0
            print("Water shortage:", shortage, "litres")
        else:
            water = available - outflow
            print("Water shortage: 0 litres")

        print("Water level:", water, "litres")

        if first_interval == 0 and water >= target:
            first_interval = i

    print("\n--- FINAL SUMMARY ---")
    print("Final water level:", water, "litres")
    print("Total overflow:", overflow_total, "litres")
    print("Total shortage:", shortage_total, "litres")

    if first_interval == 0:
        print("Target threshold was not reached.")
    else:
        print("First interval reaching target:", first_interval)
