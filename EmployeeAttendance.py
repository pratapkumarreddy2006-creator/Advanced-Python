employees = {}

while True:
    ch = input("1.Add 2.Remove 3.Display 4.Exit: ")

    if ch == "1":
        name = input("Name: ")
        employees[name] = "Present"

    elif ch == "2":
        name = input("Remove: ")
        employees.pop(name, None)

    elif ch == "3":
        print(employees)

    else:
        break