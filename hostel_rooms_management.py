hostel_rooms = {
    101:None,
    102:None,
    103:None,
    104:None

}

occupied = set()

while True:
    print("1.Locate Room")
    print("2.Allocate Room")
    print("3.Deallocate Room")
    print("4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        room_number = int(input("Enter room number to locate: "))
        if room_number in hostel_rooms:
            if hostel_rooms[room_number] is None:
                print("Room",room_number,"is available.")
            else:
                print("Room" ,room_number, "is occupied by ",hostel_rooms[room_number])
        else:
            print("Invalid room number.")
    elif choice == 2:
        room_number = int(input("Enter room number to allocate: "))
        if room_number in hostel_rooms:
            if hostel_rooms[room_number] is None:
                student_name = input("Enter student name: ")
                hostel_rooms[room_number] = student_name
                occupied.add(room_number)
                print("Room",room_number,"allocated to ",student_name)
            else:
                print("Room",room_number,"is already occupied by",hostel_rooms[room_number])
        else:
            print("Invalid room number.")
    elif choice == 3:
        room_number = int(input("Enter room number to deallocate: "))
        if room_number in hostel_rooms:
            if hostel_rooms[room_number] is not None:
                hostel_rooms[room_number] = None
                occupied.remove(room_number)
                print("Room",room_number,"deallocated successfully.")
            else:
                print("Room",room_number,"is already vacant.")
        else:
            print("Invalid room number.")
    elif choice == 4:
        print("Exiting the program.")
        break


    