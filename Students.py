
n = int(input("Enter number of students: "))

students = {}


for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks


highest_marks = max(students.values())


topper = max(students, key=students.get)


print("\nHighest Marks:", highest_marks)
print("Student with Highest Marks:", topper)