cart = {}

def add_to_cart(item, price):
    if item in cart:
        cart[item]['quantity'] += 1
    else:
        cart[item] = {'price': price, 'quantity': 1}
    print(f"Added {item} to cart.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("Your Cart:")
    for item, details in cart.items():
        print(f"{item} - ${details['price']}")


while True:
    print("\n1. Add to Cart")
    print("2. View Cart")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        add_to_cart(item, price)
    elif choice == '2':
        view_cart()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")