accounts = {
    "1001": {"name": "Rahul", "pin": "1234", "balance": 5000},
    "1002": {"name": "Anita", "pin": "5678", "balance": 8000},
    "1003": {"name": "Rohan", "pin": "4321", "balance": 3000}
}

def login():
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"\nWelcome {accounts[acc_no]['name']} ")
        return acc_no
    else:
        print("Invalid Account Number or PIN ")
        return None


def check_balance(acc_no):
    print("Your Balance is:", accounts[acc_no]["balance"])


def deposit(acc_no):
    amount = float(input("Enter amount to deposit: "))
    accounts[acc_no]["balance"] += amount
    print("Amount Deposited Successfully ")


def withdraw(acc_no):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= accounts[acc_no]["balance"]:
        accounts[acc_no]["balance"] -= amount
        print("Please collect your cash ")
    else:
        print("Insufficient Balance ")



while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Login")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = login()

        if user:
            while True:
                print("\n--- ATM Menu ---")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                option = input("Choose option: ")

                if option == "1":
                    check_balance(user)
                elif option == "2":
                    deposit(user)
                elif option == "3":
                    withdraw(user)
                elif option == "4":
                    print("Logged out successfully ")
                    break
                else:
                    print("Invalid option ")

    elif choice == "2":
        print("Thank you for using ATM ")
        break
    else:
        print("Invalid choice ")