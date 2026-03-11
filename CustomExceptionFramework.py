class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

# Product ID : [Stock, Price]
products = {
    "101": [10, 150],   # price = 150
    "102": [0, 200]     # price = 200
}

purchased = []   # list to store (pid, qty, price)

while True:
    pid = input("Enter Product ID (or type 'exit' to quit): ")

    if pid.lower() == "exit":
        break

    try:
        if pid not in products:
            raise InvalidProductIDError

        stock, price = products[pid]

        if stock == 0:
            raise OutOfStockError

        print(f"Product available (Price: ₹{price})")

        choice = input("Do you want to buy it? (yes/no): ")

        if choice.lower() == "yes":
            qty = int(input("Enter quantity: "))

            if qty > stock:
                print("Sorry, not enough stock available.")
                continue

            # Deduct stock
            products[pid][0] -= qty

            # Add to purchase list
            purchased.append((pid, qty, price))

            print("Added to cart.\n")
        else:
            print("Not added.\n")

    except InvalidProductIDError:
        print("Invalid Product ID\n")

    except OutOfStockError:
        print("Product out of stock\n")

# -----------------------------------
# FINAL BILL SECTION
# -----------------------------------
print("\n=========== FINAL BILL ===========")

if purchased:
    total = 0
    for pid, qty, price in purchased:
        amount = qty * price
        total += amount
        print(f"Product {pid} | Qty: {qty} | Price: ₹{price} | Total: ₹{amount}")

    print("----------------------------------")
    print(f"Grand Total: ₹{total}")
else:
    print("No items purchased.")

print("\n=========== UPDATED STOCK ===========")
for pid, data in products.items():
    print(f"Product {pid}: {data[0]} left")