students = {}

def add_student():
    try:
        sid = int(input("Enter Student ID: "))
        grade = float(input("Enter Grade: "))

        if sid in students:
            raise Exception("Student ID already exists")

        students[sid] = grade
        print("Student added successfully")

    except ValueError:
        print("Invalid input! ID must be integer and grade must be number")

def update_student():
    try:
        sid = int(input("Enter Student ID to update: "))

        if sid not in students:
            raise KeyError("Student ID not found")

        grade = float(input("Enter new grade: "))
        students[sid] = grade
        print("Grade updated")

    except KeyError:
        print("Invalid Student ID")

def delete_student():
    try:
        sid = int(input("Enter Student ID to delete: "))
        del students[sid]
        print("Student deleted")

    except KeyError:
        print("Student ID does not exist")

while True:
    print("\n1.Add 2.Update 3.Delete 4.View 5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        update_student()
    elif ch == "3":
        delete_student()
    elif ch == "4":
        print("Current Students:", students)
    elif ch == "5":
        break
    else:
        print("Invalid choice!")


print("\n=== Final Student Data ===")
if students:
    for sid, grade in students.items():
        print(f"ID: {sid}  →  Grade: {grade}")
else:
    print("No students added.")