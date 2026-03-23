class StudentRecordSystem:
    """Manage student records with marks tracking and statistics."""
    
    def __init__(self):
        """Initialize the student record system."""
        self.students = {}
    
    def add_student(self, name, marks):
        """Add or update a student record.
        
        Args:
            name: Student's name
            marks: List of marks (int or float)
        
        Raises:
            ValueError: If name empty, marks empty, or invalid values
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string")
        
        if not isinstance(marks, list) or len(marks) == 0:
            raise ValueError("Marks must be a non-empty list")
        
        normalized_name = name.strip()
        validated_marks = []
        for m in marks:
            if not isinstance(m, (int, float)):
                raise ValueError(f"Invalid mark: {m!r}. Must be int or float")
            if not (0 <= m <= 100):
                raise ValueError(f"Mark {m} must be between 0 and 100")
            validated_marks.append(float(m))
        
        self.students[normalized_name] = validated_marks
    
    def add_marks(self, name, new_marks):
        """Add additional marks to a student's record.
        
        Args:
            name: Student's name
            new_marks: Single mark or list of marks to add
        
        Raises:
            KeyError: If student not found
            ValueError: If marks invalid
        """
        normalized_name = name.strip()
        if normalized_name not in self.students:
            raise KeyError(f"Student {name!r} not found")
        
        if isinstance(new_marks, (int, float)):
            new_marks = [new_marks]
        
        if not isinstance(new_marks, list):
            raise ValueError("Marks must be a number or list of numbers")
        
        for m in new_marks:
            if not isinstance(m, (int, float)) or not (0 <= m <= 100):
                raise ValueError(f"Invalid mark: {m}. Must be number between 0-100")
        
        self.students[normalized_name].extend(new_marks)
    
    def remove_student(self, name):
        """Remove a student from the system.
        
        Args:
            name: Student's name
        
        Returns:
            True if removed, False if not found
        """
        normalized_name = name.strip()
        if normalized_name in self.students:
            del self.students[normalized_name]
            return True
        return False
    
    def get_average(self, name):
        """Calculate average marks for a student.
        
        Args:
            name: Student's name
        
        Returns:
            Average marks (float)
        
        Raises:
            KeyError: If student not found
        """
        normalized_name = name.strip()
        if normalized_name not in self.students:
            raise KeyError(f"Student {name!r} not found")
        
        marks = self.students[normalized_name]
        if not marks:
            raise ValueError(f"Student {name!r} has no marks")
        
        return sum(marks) / len(marks)
    
    def get_topper(self):
        """Get the student with highest average.
        
        Returns:
            Student name with highest average, or None if no students
        """
        if not self.students:
            return None
        return max(self.students, key=self.get_average)
    
    def get_statistics(self):
        """Get overall statistics.
        
        Returns:
            Dict with count, highest avg, lowest avg, class avg
        """
        if not self.students:
            return {
                "total_students": 0,
                "class_average": 0,
                "highest_average": None,
                "lowest_average": None,
                "topper": None
            }
        
        averages = [self.get_average(name) for name in self.students]
        
        return {
            "total_students": len(self.students),
            "class_average": round(sum(averages) / len(averages), 2),
            "highest_average": round(max(averages), 2),
            "lowest_average": round(min(averages), 2),
            "topper": self.get_topper()
        }
    
    def print_report(self):
        """Print detailed report of all students."""
        if not self.students:
            print("No students available.")
            return
        
        print("\n" + "="*50)
        print("STUDENT RECORD REPORT")
        print("="*50)
        
        for name in sorted(self.students):
            avg = self.get_average(name)
            marks_str = ', '.join(f"{m:.0f}" for m in self.students[name])
            print(f"{name:20s} | Marks: {marks_str:20s} | Avg: {avg:.2f}")
        
        stats = self.get_statistics()
        print("="*50)
        print(f"Class Average: {stats['class_average']}")
        print(f"Topper: {stats['topper']} ({stats['highest_average']:.2f})")
        print("="*50 + "\n")


if __name__ == "__main__":
    system = StudentRecordSystem()
    
    # Add students
    system.add_student("A", [80, 90])
    system.add_student("B", [95, 85])
    
    # Print report
    system.print_report()
    
    # Add more marks to student A
    system.add_marks("A", 88)
    print(f"Updated A's average: {system.get_average('A'):.2f}")
    
    # Get statistics
    stats = system.get_statistics()
    print(f"Total Students: {stats['total_students']}")
    print(f"Highest Average: {stats['highest_average']}")