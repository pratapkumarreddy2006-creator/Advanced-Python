menu = {"pizza": 100, "burger": 50, "cola": 30}
total = 0

while True:
    item = input("Enter item (or exit): ")
    if item == "exit":
        break
    if item in menu:
        total += menu[item]

tax = total * 0.05
print("Total:", total + tax)