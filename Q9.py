string = input("Enter a string: ")

result = ""
capitalize = True

for ch in string:
    if capitalize and ch.isalpha():
        result += ch.upper()
        capitalize = False
    else:
        result += ch
        if ch == " ":
            capitalize = True

print("Result:", result)
