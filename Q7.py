string = input("Enter a string: ")

result = ""
vowels = "aeiouAEIOU"

for ch in string:
    if ch not in vowels:
        result += ch

print("String after removing vowels:", result)
