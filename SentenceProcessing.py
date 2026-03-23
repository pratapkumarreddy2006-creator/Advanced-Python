s = input("Enter sentence: ")

vowels = "aeiouAEIOU"
v = sum(1 for ch in s if ch in vowels)
c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)

print("Vowels:", v)
print("Consonants:", c)
print("Reverse:", s[::-1])
print("Replace spaces:", s.replace(" ", "_"))
print("Capitalized:", s.title())