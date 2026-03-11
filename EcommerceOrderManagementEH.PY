stock = 5
coupon = "SAVE10"
orders = []      

try:
    quantity = int(input("Enter quantity: "))

    if quantity > stock:
        raise Exception("Out of stock")

    code = input("Enter coupon code (optional): ")

   
    price_per_item = 100
    total_price = quantity * price_per_item


    if code == coupon:
        discount = total_price * 0.10
        total_price -= discount
        coupon_msg = "Discount applied (10%)"
    elif code == "":
        coupon_msg = "No coupon used"
    else:
        raise ValueError("Invalid coupon code")

    payment = input("Enter payment method (card/upi): ")

    if payment not in ["card", "upi"]:
        raise Exception("Invalid payment method")

    stock -= quantity

    orders.append(
        f"Ordered {quantity} item(s) | Payment: {payment} | {coupon_msg} | Final Amount: {total_price}"
    )

    print("Order placed successfully")

except ValueError as e:
    print(e)

except Exception as e:
    print(e)


print("\n=== Order Summary ===")

if orders:
    for o in orders:       
        print("-", o)
else:
    print("No orders placed.")

print("Final Stock:", stock)