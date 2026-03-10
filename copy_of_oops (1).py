class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.marks = []

    def enter_marks(self):
        print("Enter marks for", self.name)
        for i in range(self.subjects):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)

    def calculate_cgpa(self):
        total = sum(self.marks)
        average = total / self.subjects
        cgpa = average / 10
        return cgpa

    def display(self):
        cgpa = self.calculate_cgpa()
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)
        print("CGPA:", round(cgpa, 2))


name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

s1 = Student(name, subjects)
s1.enter_marks()
s1.display()

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, site, password):
        self.passwords[site] = password

    def get_password(self, site):
        print("Password:", self.passwords.get(site, "Not found"))


pm = PasswordManager()
pm.add_password("gmail", "")
pm.get_password("gmail")

class Freelancer:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

class Project:
    def __init__(self, title):
        self.title = title

    def assign(self, freelancer):
        print(f"{freelancer.name} assigned to {self.title}")


f1 = Freelancer("Satya", "Python")
p1 = Project("Website")
p1.assign(f1)

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Warehouse:
    def __init__(self):
        self.inventory = {}


    def add_product(self, name, qty):
        if name in self.inventory:
            self.inventory[name].quantity += qty
        else:
            self.inventory[name] = Product(name, qty)
        print(qty, name, "added to warehouse")


    def remove_product(self, name, qty):
        if name in self.inventory and self.inventory[name].quantity >= qty:
            self.inventory[name].quantity -= qty
            print(qty, name, "removed from warehouse")
        else:
            print("Not enough stock")


    def generate_report(self):
        print("\nInventory Report")
        for product in self.inventory.values():
            print(product.name, ":", product.quantity)


    def forecast_demand(self):
        print("\nDemand Forecast")
        for product in self.inventory.values():
            forecast = product.quantity + 10
            print("Expected demand for", product.name, "=", forecast)


w = Warehouse()
w.add_product("Laptop", 20)
w.add_product("Mouse", 50)
w.remove_product("Laptop", 5)
w.generate_report()
w.forecast_demand()


class ParkingLot:
    def __init__(self, total_spots, rate_per_hour=20):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.vehicles = {}  
        self.rate_per_hour = rate_per_hour
        self.current_time = 0 

    def tick(self, hours=1):
        """Simulate time passing."""
        self.current_time += hours

    def vehicle_entry(self, vehicle_number):
        if self.available_spots > 0:
            self.vehicles[vehicle_number] = self.current_time
            self.available_spots -= 1
            print(f"Vehicle {vehicle_number} entered at {self.current_time} hrs. Spots left: {self.available_spots}")
        else:
            print("Parking Full! No spots available.")

    def vehicle_exit(self, vehicle_number):
        if vehicle_number in self.vehicles:
            entry_time = self.vehicles.pop(vehicle_number)
            self.available_spots += 1

            duration = self.current_time - entry_time
            fee = duration * self.rate_per_hour

            print(f"Vehicle {vehicle_number} exited at {self.current_time} hrs. Duration: {duration} hrs. Fee: ₹{fee}")
        else:
            print("Vehicle not found in parking records.")

    def status(self):
        print(f"Total spots: {self.total_spots}, Available spots: {self.available_spots}")
        print(f"Currently parked vehicles: {list(self.vehicles.keys())}")


if __name__ == "__main__":
    lot = ParkingLot(total_spots=3, rate_per_hour=30)
    lot.vehicle_entry("OD-02-AB-1234")
    lot.vehicle_entry("OD-05-CD-5678")
    lot.status()
    lot.tick(2)
    lot.vehicle_exit("OD-14-1b-6565")
    lot.status()


# 2 To-Do List Manager with Categories
tasks = []

def add_task(title, category, priority, deadline, tags):
    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "deadline": deadline,
        "tags": tags,
        "completed": False
    }
    tasks.append(task)

def show_tasks():
    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(i+1, task["title"], task["category"], task["priority"], task["deadline"], status)

def filter_category(category):
    for task in tasks:
        if task["category"] == category:
            print(task["title"])

def filter_tag(tag):
    for task in tasks:
        if tag in task["tags"]:
            print(task["title"])




# 3 Billing system Retail store
products = {
    101: {"name": "Milk", "price": 50},
    102: {"name": "Bread", "price": 30},
}

cart = []

def add_product(pid, qty):
    if pid in products:
        item = products[pid]
        total = item["price"] * qty
        cart.append((item["name"], qty, total))

def generate_bill():
    total = 0
    print("----- BILL -----")
    for name, qty, price in cart:
        print(name, qty, price)
        total += price
    print("Total:", total)


# 4 Booking movie
movies = {
    "Avengers": ["10:00 AM", "1:00 PM"],
    "Batman": ["11:00 AM", "3:00 PM"]
}

seats = ["O"] * 10

def show_movies():
    print("Available Movies:")
    for i, movie in enumerate(movies):
        print(i+1, movie)

def show_showtimes(movie):
    print("Showtimes:")
    for time in movies[movie]:
        print(time)

def show_seats():
    print("Seats:")
    for i, seat in enumerate(seats):
        print(f"{i+1}: {seat}")

def book_seat(num):
    if seats[num-1] == "O":
        seats[num-1] = "X"
        print("Seat booked successfully!")
    else:
        print("Seat already booked")


# 10 online exam
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer


class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0


questions = []
students = []


def add_question():
    q = input("Enter question: ")
    options = []

    for i in range(4):
        opt = input(f"Option {i+1}: ")
        options.append(opt)

    answer = int(input("Correct option number (1-4): "))
    questions.append(Question(q, options, answer))

    print("Question added successfully.")


def register_student():
    name = input("Enter student name: ")
    students.append(Student(name))
    print("Student registered.")


def start_exam():
    name = input("Enter student name: ")

    student = None
    for s in students:
        if s.name == name:
            student = s
            break

    if not student:
        print("Student not registered.")
        return

    score = 0

    for q in questions:
        print("\n", q.question)

        for i, opt in enumerate(q.options):
            print(f"{i+1}. {opt}")

        ans = int(input("Your answer: "))

        if ans == q.answer:
            score += 1

    student.score = score
    print("Exam completed!")


def show_results():
    print("\n--- Results ---")

    for s in students:
        print(f"{s.name} : {s.score}/{len(questions)}")


while True:
    print("\n===== ONLINE EXAMINATION SYSTEM =====")
    print("1. Add Question")
    print("2. Register Student")
    print("3. Start Exam")
    print("4. Show Results")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_question()

    elif choice == "2":
        register_student()

    elif choice == "3":
        start_exam()

    elif choice == "4":
        show_results()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

