string = input("Enter a string: ")
ch = input("Enter the character to find: ")

first = string.find(ch)
last = string.rfind(ch)

if first == -1:
    print("Character not found in the string")
else:
    print("First occurrence at index:", first)
    print("Last occurrence at index:", last)
