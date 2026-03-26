lst = [3, 7, 2, 9, 5]
largest = lst[0]

for i in lst:
    if i > largest:
        largest = i

print(largest)