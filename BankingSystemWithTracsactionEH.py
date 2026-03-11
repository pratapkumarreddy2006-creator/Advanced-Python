balance = 1000
updates = []      
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount > balance:
            raise Exception("Overdraft! Not enough balance")

        if amount <= 0:
            raise ValueError("Invalid amount")

        balance -= amount
        updates.append(f"Withdrawn: {amount}")
        print("Withdrawal successful")
        print("Remaining balance:", balance)

    except ValueError:
        print("Enter valid amount")
    except Exception as e:
        print(e)

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            raise ValueError("Invalid amount")

        balance += amount
        updates.append(f"Deposited: {amount}")
        print("Deposit successful")
        print("Updated balance:", balance)

    except ValueError:
        print("Enter valid amount")


while True:
    print("\n1. Withdraw  2. Deposit  3. View Balance  4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        withdraw()
    elif ch == "2":
        deposit()
    elif ch == "3":
        print("Current Balance:", balance)
    elif ch == "4":
        break
    else:
        print("Invalid choice!")
print("\n=== Session Summary ===")

if updates:
    print("Your Transactions:")
    for u in updates:       
        print(" -", u)
else:
    print("No transactions done.")

print("\nFinal Balance:", balance)