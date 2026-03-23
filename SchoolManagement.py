class Student:
    """Represents a student in the school."""
    
    def __init__(self, name, student_id):
        """Initialize a student.
        
        Args:
            name: Student's name
            student_id: Unique identifier for student
        
        Raises:
            ValueError: If name is empty or student_id is not positive
        """
        if not name or not isinstance(name, str):
            raise ValueError("Student name must be a non-empty string")
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student ID must be a positive integer")
        
        self.name = name
        self.student_id = student_id
        self.marks = {}
    
    def add_marks(self, subject, marks):
        """Record marks for a subject.
        
        Args:
            subject: Subject name
            marks: Marks scored (0-100)
        
        Raises:
            ValueError: If marks not in valid range
        """
        if not isinstance(marks, (int, float)) or not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.marks[subject] = marks
    
    def __repr__(self):
        return f"Student(id={self.student_id}, name='{self.name}')"


class Teacher:
    """Represents a teacher in the school."""
    
    def __init__(self, name, subject, employee_id):
        """Initialize a teacher.
        
        Args:
            name: Teacher's name
            subject: Subject taught
            employee_id: Unique identifier
        
        Raises:
            ValueError: If name/subject empty or employee_id invalid
        """
        if not name or not isinstance(name, str):
            raise ValueError("Teacher name must be a non-empty string")
        if not subject or not isinstance(subject, str):
            raise ValueError("Subject must be a non-empty string")
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
        
        self.name = name
        self.subject = subject
        self.employee_id = employee_id
    
    def __repr__(self):
        return f"Teacher(id={self.employee_id}, name='{self.name}', subject='{self.subject}')"


class Admin:
    """Represents administrative staff managing the school system."""
    
    def __init__(self, name, admin_id):
        """Initialize admin.
        
        Args:
            name: Admin's name
            admin_id: Unique identifier
        """
        if not name or not isinstance(name, str):
            raise ValueError("Admin name must be a non-empty string")
        if not isinstance(admin_id, int) or admin_id <= 0:
            raise ValueError("Admin ID must be a positive integer")
        
        self.name = name
        self.admin_id = admin_id
    
    def manage(self, school):
        """Manage school operations.
        
        Args:
            school: School instance to manage
        """
        if not isinstance(school, School):
            raise ValueError("Must provide a School instance")
        
        print(f"Admin {self.name} managing school system")
        print(f"  Total students: {len(school.students)}")
        print(f"  Total teachers: {len(school.teachers)}")
    
    def __repr__(self):
        return f"Admin(id={self.admin_id}, name='{self.name}')"


class School:
    """Manages students, teachers, and administrative systems."""
    
    def __init__(self, name):
        """Initialize a school.
        
        Args:
            name: School name
        """
        if not name or not isinstance(name, str):
            raise ValueError("School name must be a non-empty string")
        
        self.name = name
        self.students = {}
        self.teachers = {}
        self.admin = None
    
    def add_student(self, student):
        """Add a student to the school.
        
        Args:
            student: Student instance
        """
        if not isinstance(student, Student):
            raise ValueError("Must provide a Student instance")
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists")
        
        self.students[student.student_id] = student
    
    def add_teacher(self, teacher):
        """Add a teacher to the school.
        
        Args:
            teacher: Teacher instance
        """
        if not isinstance(teacher, Teacher):
            raise ValueError("Must provide a Teacher instance")
        if teacher.employee_id in self.teachers:
            raise ValueError(f"Teacher with ID {teacher.employee_id} already exists")
        
        self.teachers[teacher.employee_id] = teacher
    
    def set_admin(self, admin):
        """Set the admin for the school.
        
        Args:
            admin: Admin instance
        """
        if not isinstance(admin, Admin):
            raise ValueError("Must provide an Admin instance")
        self.admin = admin
    
    def get_student(self, student_id):
        """Retrieve student by ID.
        
        Args:
            student_id: Student's ID
        
        Returns:
            Student instance or None if not found
        """
        return self.students.get(student_id)
    
    def display_students(self):
        """Display all registered students."""
        if not self.students:
            print("No students registered")
            return
        
        print(f"\n{self.name} - Registered Students:")
        for student_id, student in self.students.items():
            print(f"  {student}")
    
    def display_teachers(self):
        """Display all registered teachers."""
        if not self.teachers:
            print("No teachers registered")
            return
        
        print(f"\n{self.name} - Registered Teachers:")
        for emp_id, teacher in self.teachers.items():
            print(f"  {teacher}")


if __name__ == "__main__":
    # Create school
    school = School("Central High School")
    
    # Add students
    s1 = Student("Alice", 101)
    s2 = Student("Bob", 102)
    school.add_student(s1)
    school.add_student(s2)
    
    # Add teachers
    t1 = Teacher("Mr. Smith", "Math", 1001)
    t2 = Teacher("Ms. Johnson", "English", 1002)
    school.add_teacher(t1)
    school.add_teacher(t2)
    
    # Add admin
    admin = Admin("John Carter", 2001)
    school.set_admin(admin)
    
    # Display information
    school.display_students()
    school.display_teachers()
    
    # Admin management
    admin.manage(school)
