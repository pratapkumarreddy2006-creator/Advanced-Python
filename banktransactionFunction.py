USERNAME = "deba"
PASSWORD = "9090"

attempts = 3
while attempts > 0:
    user = input("Enter username:")
    pss = input("Enter Password:")
    if user == USERNAME and pss == PASSWORD:
        print("Logged in successfully")
        break
    else:
        attempts -= 1
        print("Invalid credentials Attempts left: ",attempts)

    if attempts == 0:
        print("Too many failed attempts. Account locked")
        exit()
    
global balance
balance = 0
transaction = []
def deposit():
        amount = int(input("Enter The Amount"))
        global balance  
        balance = balance+amount
        transaction.append(amount)
        print("amount deposited")
        

def withdraw():
    amount = int(input("Enter the withdraw amount"))
    global balance
    if(balance>amount):
        balance = balance-amount
    else:
        print("Insufficient Balance")
        
def check_bal():
    print("Your current balace is",balance)
def ext():
    exit()
while True:
    print("/n1.Deposite")
    print("/n2.Withdraw")
    print("/n3.Check Balance")
    print("/n4.Transaction")
    print("/n5.Exit")
    choice = int(input("Enter your choice"))

    if(choice==1):
        deposit()
    elif(choice==2):
        withdraw()
    elif(choice==3):
        check_bal()
    elif(choice==5):
        ext()