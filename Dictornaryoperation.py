students = {"A": 90, "B": 80}

students["C"] = 85        # add
students["A"] = 95        # update
del students["B"]         # delete

print("Keys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())