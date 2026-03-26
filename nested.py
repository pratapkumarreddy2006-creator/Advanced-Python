lst = [[1, 2], [3, 4], [5]]
flat = []

for sub in lst:
    for i in sub:
        flat.append(i)

print(flat)