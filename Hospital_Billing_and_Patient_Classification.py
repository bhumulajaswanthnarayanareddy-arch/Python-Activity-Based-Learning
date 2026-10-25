

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
card = input("Valid concession card? (yes/no): ").lower()

consultation = float(input("Consultation charges: Rs. "))
diagnostic = float(input("Diagnostic charges: Rs. "))
treatment = float(input("Treatment charges: Rs. "))


if (age < 0 or consultation < 0
        or diagnostic < 0 or treatment < 0):
    print("Invalid input: age and charges cannot be negative.")

elif card != "yes" and card != "no":
    print("Invalid concession card status.")

else:
    # Calculate total bill
    charges = [consultation, diagnostic, treatment]
    total = 0

    for charge in charges:
        total = total + charge

    # Apply concession
    if card == "yes":
        concession_rate = 15
    elif age >= 60:
        concession_rate = 10
    else:
        concession_rate = 0

    concession = total * concession_rate / 100
    final_bill = total - concession

    # Classify patient bill
    if final_bill >= 10000:
        category = "High Bill"
    elif final_bill >= 5000:
        category = "Medium Bill"
    else:
        category = "Low Bill"

    
    print("\n--- HOSPITAL BILL ---")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)
    print("Total Bill: Rs.", total)
    print("Concession:", concession_rate, "%")
    print("Concession Amount: Rs.", concession)
    print("Final Bill: Rs.", final_bill)
    print("Payment Classification:", category)
