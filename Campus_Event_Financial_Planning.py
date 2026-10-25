

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificates = float(input("Enter certificate cost: Rs. "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship received: Rs. "))
target_sponsorship = float(input("Enter target sponsorship: Rs. "))
registration_fee = float(input("Enter registration fee per person: Rs. "))


costs = [venue, equipment, catering, transport, certificates]

valid = True

for cost in costs:
    if cost < 0:
        valid = False

if (participants < 0 or sponsorship < 0
        or target_sponsorship < 0 or registration_fee <= 0):
    valid = False

if not valid:
    print("Invalid input. Costs and amounts must be non-negative,")
    print("participants cannot be negative, and registration fee must be positive.")

else:
    
    total_cost = 0

    for cost in costs:
        total_cost = total_cost + cost


    remaining_cost = total_cost - sponsorship

    if remaining_cost < 0:
        remaining_cost = 0


    if participants > 0:
        contribution = remaining_cost / participants
    else:
        contribution = 0

    # Calculate sponsorship shortfall
    shortfall = target_sponsorship - sponsorship

    if shortfall < 0:
        shortfall = 0

    # Calculate break-even registrations using a loop
    collected = 0
    registrations = 0

    while collected < remaining_cost:
        collected = collected + registration_fee
        registrations = registrations + 1

    
    print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
    print("Total Event Cost: Rs.", round(total_cost, 2))
    print("Sponsorship Received: Rs.", round(sponsorship, 2))
    print("Remaining Cost: Rs.", round(remaining_cost, 2))
    print("Contribution per Expected Participant: Rs.",
          round(contribution, 2))
    print("Sponsorship Shortfall: Rs.", round(shortfall, 2))
    print("Registration Fee: Rs.", round(registration_fee, 2))
    print("Minimum Break-Even Registrations:", registrations)

    if participants >= registrations:
        print("Status: Expected registrations can cover the remaining cost.")
    else:
        print("Status: More registrations are needed to break even.")
