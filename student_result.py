students = []

while True:
    print("\n1. Add Student")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student Name: ")
        marks = float(input("Marks (out of 100): "))

        percentage = marks
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        students.append([name, percentage, grade])

    elif choice == "2":
        print("\nResults:")
        for s in students:
            print(f"Name: {s[0]}, Percentage: {s[1]}%, Grade: {s[2]}")

    elif choice == "3":
        break