balance = 0
transaction = []

USERNAME = "admin"
PASSWORD = "1234"


attempts = 3
while attempts > 0:
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("\nLogin successful \n")
        break
    else:
        attempts -= 1
        print("Invalid credentials Attempts left: ",attempts)

if attempts == 0:
    print("\nToo many failed attempts. Account locked")
    exit()


while True:
    print("/n1.Deposite")
    print("/n2.Withdraw")
    print("/n3.Check Balance")
    print("/n4.Transaction")
    print("/n5.Exit")
    choice = int(input("Enter your choice"))
    
    if(choice==1):
        amt = int(input("Enter The Amount"))
        balance = balance+amt
        transaction.append(amt)
        print("amount deposited")

    elif(choice==2):
        wamt = int(input("Enter the withdraw amount"))
        if(balance>wamt):
            balance = balance-wamt
        else:
            print("Insufficient Balance")
    elif(choice==3):
        print("Your current balace is",balance)
    elif(choice==5):
        break
