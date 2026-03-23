s = input("Enter string: ")

for ch in set(s):
    if s.count(ch) == 1 and ch.isalnum():
        print(ch)