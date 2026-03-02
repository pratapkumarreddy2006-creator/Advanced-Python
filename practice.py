fruits = ["Mango","Banana","Coconut"]

fruits_rev = []
for fr in fruits:
    fruits.append(fruits_rev(fr[::-1]))

print("Reversed fruits:",fruits_rev)