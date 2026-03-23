# Simple ATM Simulation

balance = 1000   # initial balance
pin = "1234"     # hardcoded PIN

# Login (Optional Bonus)
user_pin = input("Enter your PIN: ")

if user_pin != pin:
    print("Incorrect PIN. Access Denied.")
else:
    print("Login Successful!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your current balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance = balance + amount
            print("Deposit successful!")
            print("Updated balance:", balance)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance = balance - amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")