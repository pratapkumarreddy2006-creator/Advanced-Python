words = ["madam", "hello", "racecar", "python code"]

sorted_words = sorted(words, key=len)
palindromes = [w for w in words if w == w[::-1]]
hyphen = [w.replace(" ", "-") for w in words]

print(sorted_words)
print("Palindromes:", palindromes)
print(hyphen)