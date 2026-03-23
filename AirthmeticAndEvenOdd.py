a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)

print("a is Even" if a % 2 == 0 else "a is Odd")
print("Float value of a:", float(a))