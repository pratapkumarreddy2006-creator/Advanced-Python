lst = [1, 2, 2, 3, 1]

freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)