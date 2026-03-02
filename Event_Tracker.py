entered_std = set()
rejected_std = set()

n = int(input("Enter Entry Attempts: "))

for i in range(n):
    name = input("Enter students name: ")
    
    name = name.strip().lower()        

    if name in entered_std:
        print(name, "Already entered. Entry Rejected")
        rejected_std.add(name)
    

    else:
        print(name, "Entry Allowed")
        entered_std.add(name)

print("-- Event Tracker --")

print("-- Total Entered Student")
for name in entered_std:
    print(name)

print("--Total Rejected Student--")
for name in rejected_std:
    print(name)

print("Unique Entries :", len(entered_std))

#convert name to lowercase
#remove whitespace
#date n time           
#password or smthng


