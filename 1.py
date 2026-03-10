cart = {}   
def add_item():
    item = input("Enter item name: ").lower()
    price = float(input("Enter item price in numeric value : "))
    cart[item] = cart.get(item,0)+price
    print(item, "added to cart with !\n",item)

def remove_item():
    item = input("Enter item name to remove: ").lower()
    if item in cart:
        del cart[item]
        print(item, "removed from cart!\n")
    else:
        print("Item not found!\n")

def display_bill():
    print("\n------ BILL DETAILS ------")
    total = sum(cart.values())

    for item, price in cart.items():
        print(f"{item} : ₹{price}")

    print("--------------------------")
    print("Total Price:", total)

    # Discount rules
    if total > 5000:
        discount = 20
    elif total > 3000:
        discount = 15
    elif total > 1000:
        discount = 10
    else:
        discount = 5

    print("Discount Percentage:", discount, "%")

    final_price = total - (total * discount / 100)
    print("Final Price After Discount:", final_price)
    print("--------------------------")


while True:
    print("\n press'1'  for Adding items  ")
    print("\n press '2' for removing items ")
    print("\n'press 3'for Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        display_bill()
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice!")