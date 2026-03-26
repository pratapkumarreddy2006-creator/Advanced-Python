lst = [1, 2, 3, 4, 5]
target = 6

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])