seats = 10
price_per_seat = 500

booked_passengers = []    
next_seat_number = 1      

while True:
    print("\nType 'exit' anytime to stop booking.")
    user_input = input("Enter number of passengers: ")

    if user_input.lower() == "exit":
        break

    try:
        passengers = int(user_input)

        if passengers > seats:
            raise Exception("Seats not available")

        name = input("Enter passenger name: ")
        if name.lower() == "exit":
            break

        if name.strip() == "":
            raise ValueError("Invalid passenger details")

        payment = input("Payment success? (yes/no): ")
        if payment.lower() == "exit":
            break

        if payment != "yes":
            raise Exception("Payment failure")

       
        total_amount = passengers * price_per_seat

        
        seat_numbers = list(range(next_seat_number, next_seat_number + passengers))
        next_seat_number += passengers

        print("Flight booked successfully!")
        print(f"Seats Allotted: {seat_numbers}")
        print(f"Amount to Pay: ₹{total_amount}\n")

        seats -= passengers  

        booked_passengers.append((name, passengers, seat_numbers, total_amount))

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)



print("\n======= FINAL SUMMARY =======")

if booked_passengers:
    for name, qty, seats_list, amount in booked_passengers:
        print(f"Passenger Name : {name}")
        print(f"Seats Booked   : {qty}")
        print(f"Seat Numbers   : {seats_list}")
        print(f"Amount Paid    : ₹{amount}")
        print("----------------------------------")
else:
    print("No passengers booked.")

print(f"\nRemaining Seats: {seats}")