

attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
threshold = float(input("Enter required attendance percentage: "))

if (conducted < 0 or attended < 0 or attended > conducted
        or threshold <= 0 or threshold > 100):
    print("Invalid attendance details.")

else:
    if conducted == 0:
        current = 0
    else:
        current = attended / conducted * 100

    print("Current attendance:", round(current, 2), "%")

    if current >= threshold:
        print("Attendance requirement already satisfied.")
    else:
        
        a = attended
        t = conducted
        classes = 0

        while a / t * 100 < threshold:
            a += 1
            t += 1
            classes += 1

        print("Attend every class: minimum", classes, "classes")

        
        a = attended
        t = conducted
        classes = 0
        future_attended = 0

        while a / t * 100 < threshold and classes < 100000:
            classes += 1

        
            if classes % 10 != 0:
                a += 1
                future_attended += 1

            t += 1

        if a / t * 100 >= threshold:
            print("Attend 90% of future classes: minimum",
                  classes, "future classes")
        else:
            print("Target not reached in the simulation limit.")
