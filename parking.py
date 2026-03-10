import time

parking = {}
rate_per_hour = 20

def park_vehicle():
    number = input("Enter vehicle number: ")
    entry_time = time.time()
    parking[number] = entry_time
    print("Vehicle parked successfully")

def exit_vehicle():
    number = input("Enter vehicle number: ")
    
    if number in parking:
        entry_time = parking[number]
        exit_time = time.time()
        hours = (exit_time - entry_time) / 3600
        fee = round(hours * rate_per_hour, 2)

        print("Parking Fee:", fee)
        del parking[number]
    else:
        print("Vehicle not found")

def show_vehicles():
    print("Parked Vehicles:", parking.keys())

while True:
    print("\n1.Park Vehicle\n2.Exit Vehicle\n3.Show Vehicles\n4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        park_vehicle()
    elif choice == "2":
        exit_vehicle()
    elif choice == "3":
        show_vehicles()
    else:
        break