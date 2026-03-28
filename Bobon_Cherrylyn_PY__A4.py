def add_record():
    file = open("records.txt", "a")  # append mode
    name = input("Enter student name: ")
    grade = input("Enter grade: ")

    file.write(name + " - " + grade + "\n")
    file.close()

    print("Record saved successfully!\n")


def view_records():
    try:
        file = open("records.txt", "r")
        data = file.read()
        file.close()

        print("\n--- Student Records ---")
        print(data)

    except FileNotFoundError:
        print("No records found.\n")


while True:
    print("1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.\n")d
