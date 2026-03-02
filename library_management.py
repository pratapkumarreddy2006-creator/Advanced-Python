book_id = {
    "b1":{
        "Author":"Atomic Habits",
        "Title":"james Clear",
        "availability":None    
    },
    "b2":{
        "Author":"Introduction to Algorithms",
        "Title":"Thomas H. Cormen",
        "availability":None
    },
    "b3":{
        "Author":"Peter Thiel",
        "Title":"Zero to One",
        "availability":None
    },
    "b4":{
        "Author":"Sapiens",
        "Title":"Yuval Noah Harari",
        "availability":None
    }
}

taken = set()   

while True:
    print("1.Locate Book")
    print("2.Issue Book")
    print("3.Return Book")
    print("4.Details")
    print("5.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_code = input("Enter book ID to locate: ")
        if book_code in book_id:
            if book_id[book_code]["availability"] is None:
                print("Book",book_code,"is available.")
            else:
                print("Book",book_code,"is issued to",book_id[book_code]["availability"])
        else:
            print("Invalid book ID.")
    elif choice == 2:
        book_code = input("Enter book ID to issue: ")
        if book_code in book_id:
            if book_id[book_code]["availability"] is None:
                student_name = input("Enter student name: ")
                book_id[book_code]["availability"] = student_name
                taken.add(book_code)
                print("Book",book_code,"issued to",student_name)
            else:
                print("Book",book_code,"is already issued to",book_id[book_code]["availability"])
        else:
            print("Invalid book ID.")
    elif choice == 3:
        book_code = input("Enter book ID to return: ")
        if book_code in book_id:
            if book_id[book_code]["availability"] is not None:
                book_id[book_code]["availability"] = None
                taken.remove(book_code)
                print("Book",book_code,"returned successfully.")
            else:
                print("Book",book_code,"is not issued to anyone.")
        else:
            print("Invalid book ID.")
    elif choice == 4:
        bid = input("Enter book ID to view details before exiting: ")
        if bid in book_id:
            print("Book ID:", bid)
            print("Title:", book_id[bid]["Title"])
            print("Author:", book_id[bid]["Author"])
            if book_id[bid]["availability"] is None:
                print("Status: Available")
            else:
                print("Status: Issued to", book_id[bid]["availability"])
    elif choice == 5:
        print("Exiting the program.")
        break

