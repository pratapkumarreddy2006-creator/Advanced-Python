contacts = {}
changes = []    

def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        if name == "" or phone == "":
            raise ValueError("Fields cannot be empty")

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number")

        if name in contacts:
            contacts[name] = phone
            changes.append(f"Updated: {name} → {phone}")   # track update
            print("Contact updated")
        else:
            contacts[name] = phone
            changes.append(f"Added: {name} → {phone}")     # track add
            print("Contact saved")

    except ValueError as e:
        print(e)

def search_contact():
    try:
        name = input("Enter name to search: ")

        if name not in contacts:
            raise KeyError("Contact not found")

        print("Phone:", contacts[name])

    except KeyError as e:
        print(e)

while True:
    print("\n1.Add 2.Search 3.View 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        search_contact()
    elif ch == "3":
        print(contacts)
    elif ch == "4":
        break
    else:
        print("Invalid choice!")
        


print("\n=== Session Summary ===")

if changes:
    print("Changes made:")
    for c in changes:
        print(" -", c)
else:
    print("No changes made.")

print("\nFinal Contacts:")
if contacts:
    for name, phone in contacts.items():
        print(f"{name} → {phone}")
else:
    print("No contacts saved.")
