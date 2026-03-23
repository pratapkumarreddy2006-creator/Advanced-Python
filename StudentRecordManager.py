records = []

for _ in range(3):
    name = input("Name: ")
    marks = int(input("Marks: "))
    records.append({"name": name, "marks": marks})

for r in records:
    status = "Pass" if r["marks"] >= 40 else "Fail"
    print(r["name"], status)