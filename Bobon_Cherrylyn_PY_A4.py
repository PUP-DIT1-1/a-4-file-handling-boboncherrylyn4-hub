import os

FILENAME = "students.csv"

# -----------------------------
# LOAD RECORDS
# -----------------------------
def load_records():
    records = []
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()
    else:
        try:
            with open(FILENAME, "r") as file:
                for line in file:
                    if "," in line:
                        name, grade = line.strip().split(",")
                        try:
                            records.append([name, float(grade)])
                        except:
                            pass  # skip invalid lines
        except:
            print("File read error.")
    return records

# -----------------------------
# SAVE RECORDS
# -----------------------------
def save_records(records):
    try:
        with open(FILENAME, "w") as file:
            for r in records:
                file.write(f"{r[0]},{r[1]}\n")
    except:
        print("Error saving file.")

# -----------------------------
# DISPLAY RECORDS
# -----------------------------
def display_records(records):
    print("\n--- Student Records ---")
    if not records:
        print("No records yet.")
    else:
        for i, r in enumerate(records):
            print(f"{i} - {r[0]} : {r[1]}")
    print()  # extra line

# -----------------------------
# ADD RECORD
# -----------------------------
def add_record(records):
    name = input("Rodmar: ").strip()
    grade_input = input("98: ").strip()
    try:
        grade = float(grade_input)
        records.append([name, grade])
        save_records(records)
        print("Record added successfully!\n")
    except:
        print("Invalid input. Grade must be a number.\n")
        
                      
# -----------------------------
# ADD RECORD
# -----------------------------
def add_record(records):
    name = input("Joy: ").strip()
    grade_input = input("97: ").strip()
    try:
        grade = float(grade_input)
        records.append([name, grade])
        save_records(records)
        print("Record added successfully!\n")
    except:
        print("Invalid input. Grade must be a number.\n")
 
# -----------------------------
# ADD RECORD
# -----------------------------
def add_record(records):
    name = input("Stacy Fy: ").strip()
    grade_input = input("96: ").strip()
    try:
        grade = float(grade_input)
        records.append([name, grade])
        save_records(records)
        print("Record added successfully!\n")
    except:
        print("Invalid input. Grade must be a number.\n")       

# -----------------------------
# UPDATE RECORD
# -----------------------------
def update_record(records):
    display_records(records)
    if not records:
        return
    try:
        index = int(input("Enter index to update: "))
        if 0 <= index < len(records):
            name = input("Enter new name: ").strip()
            grade_input = input("Enter new grade: ").strip()
            grade = float(grade_input)
            records[index] = [name, grade]
            save_records(records)
            print("Record updated successfully!\n")
        else:
            print("Invalid index.\n")
    except:
        print("Error. Make sure index and grade are numbers.\n")

# -----------------------------
# DELETE RECORD
# -----------------------------
def delete_record(records):
    display_records(records)
    if not records:
        return
    try:
        index = int(input("Enter index to delete: "))
        if 0 <= index < len(records):
            records.pop(index)
            save_records(records)
            print("Record deleted successfully!\n")
        else:
            print("Invalid index.\n")
    except:
        print("Error. Make sure index is a number.\n")

# -----------------------------
# MAIN MENU
# -----------------------------
def main():
    records = load_records()

    while True:
        print("===== STUDENT RECORD SYSTEM =====")
        print("1 - Display Records")
        print("2 - Add Record")
        print("3 - Update Record")
        print("4 - Delete Record")
        print("5 - Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_records(records)
        elif choice == "2":
            add_record(records)
        elif choice == "3":
            update_record(records)
        elif choice == "4":
            delete_record(records)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

# RUN PROGRAM
main()
