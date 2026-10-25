
n = int(input("Enter number of subjects: "))
results = []
total_marks = 0
total_maximum = 0
all_passed = True

if n <= 0:
    print("Invalid number of subjects.")
else:
    for i in range(n):
        print("\nSubject", i + 1)
        name = input("Enter subject name: ")
        marks = float(input("Enter marks obtained: "))
        maximum = float(input("Enter maximum marks: "))
        pass_mark = float(input("Enter pass mark: "))

        if (maximum <= 0 or marks < 0 or marks > maximum
                or pass_mark < 0 or pass_mark > maximum):
            print("Invalid marks. Please check the input.")
            all_passed = False
            continue

        grace = 0

        if marks < pass_mark and pass_mark - marks <= 5:
            grace = pass_mark - marks
            marks = marks + grace

            if marks > maximum:
                marks = maximum

        if marks < pass_mark:
            status = "Fail"
            all_passed = False
        else:
            status = "Pass"

        results.append((name, marks, maximum, grace, status))
        total_marks += marks
        total_maximum += maximum

    print("\n--- EXAMINATION RESULTS ---")

    for result in results:
        name, marks, maximum, grace, status = result
        print(name, "Marks:", marks, "/", maximum,
              "Grace:", grace, "Status:", status)

    if total_maximum > 0:
        percentage = total_marks / total_maximum * 100
        print("Total:", total_marks, "/", total_maximum)
        print("Percentage:", round(percentage, 2), "%")

        if not all_passed or len(results) != n:
            print("Final Classification: FAIL")
        elif percentage >= 75:
            print("Final Classification: DISTINCTION")
        elif percentage >= 60:
            print("Final Classification: FIRST CLASS")
        elif percentage >= 50:
            print("Final Classification: SECOND CLASS")
        else:
            print("Final Classification: PASS")
