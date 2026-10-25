


for i in range(len(eligible_students)):
    best = i

    for j in range(i + 1, len(eligible_students)):
        current = eligible_students[j]
        selected = eligible_students[best]

        if current[1] > selected[1]:
            best = j

        elif current[1] == selected[1]:
            if current[2] > selected[2]:
                best = j

            elif current[2] == selected[2]:
                if current[3] < selected[3]:
                    best = j

    temp = eligible_students[i]
    eligible_students[i] = eligible_students[best]
    eligible_students[best] = temp
