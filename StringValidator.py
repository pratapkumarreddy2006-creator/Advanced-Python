s = input("Enter string: ")

print("Palindrome:", s == s[::-1])

v = c = d = sp = 0
for ch in s:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    else:
        sp += 1

print(v, c, d, sp)