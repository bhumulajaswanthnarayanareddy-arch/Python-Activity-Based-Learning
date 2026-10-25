


vehicle = input("Enter vehicle type (car/bike/bus): ").lower()
entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")


valid = True

if len(entry) != 5 or len(exit_time) != 5:
    valid = False
else:
    if entry[2] != ":" or exit_time[2] != ":":
        valid = False
    else:
        try:
            eh = int(entry[0:2])
            em = int(entry[3:5])
            xh = int(exit_time[0:2])
            xm = int(exit_time[3:5])

            if (eh < 0 or eh > 23 or em < 0 or em > 59
                    or xh < 0 or xh > 23 or xm < 0 or xm > 59):
                valid = False
        except ValueError:
            valid = False

if vehicle == "car":
    rate = 50
    daily_limit = 300
elif vehicle == "bike":
    rate = 20
    daily_limit = 120
elif vehicle == "bus":
    rate = 100
    daily_limit = 600
else:
    valid = False

if not valid:
    print("Invalid vehicle type or time input.")
else:
    entry_minutes = eh * 60 + em
    exit_minutes = xh * 60 + xm


    if exit_minutes < entry_minutes:
        exit_minutes += 24 * 60

    duration = exit_minutes - entry_minutes

    if duration <= 0:
        print("Invalid parking duration.")
    else:
        
        hours = duration // 60

        if duration % 60 != 0:
            hours += 1

        days = hours // 24
        remaining_hours = hours % 24

        fee = days * daily_limit
        extra_fee = remaining_hours * rate

        if extra_fee > daily_limit:
            extra_fee = daily_limit

        fee += extra_fee

        penalty = 0

        if duration > 24 * 60:
            penalty = 200

        total = fee + penalty

        print("\n--- PARKING BILL ---")
        print("Vehicle:", vehicle)
        print("Parking duration:", duration, "minutes")
        print("Charged hours:", hours)
        print("Parking fee: Rs.", fee)
        print("Penalty: Rs.", penalty)
        print("Total parking charge: Rs.", total)
