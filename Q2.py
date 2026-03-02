s = input("Enter a string: ")

upper_count = 0
lower_count = 0


for ch in s:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1


print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
