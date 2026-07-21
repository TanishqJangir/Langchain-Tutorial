from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """


from datetime import datetime


class Student:
    #Represents a student.

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks.append(mark)
        else:
            raise ValueError("Marks must be between 0 and 100.")

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Average: {self.average():.2f} | "
            f"Grade: {self.grade()}"
        )


class StudentManager:
    #Manages multiple students.

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def class_average(self):
        if not self.students:
            return 0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def topper(self):
        if not self.students:
            return None

        return max(self.students, key=lambda student: student.average())

    def display_students(self):
        print("\nStudent Report")
        print("-" * 60)

        for student in self.students:
            print(student)

        print("-" * 60)
        print(f"Class Average: {self.class_average():.2f}")

        topper = self.topper()
        if topper:
            print(f"Topper: {topper.name} ({topper.average():.2f})")


def main():
    manager = StudentManager()

    data = [
        (1, "Alice", [95, 92, 88]),
        (2, "Bob", [78, 81, 76]),
        (3, "Charlie", [65, 70, 72]),
        (4, "David", [85, 89, 91]),
        (5, "Eva", [55, 60, 58]),
    ]

    for student_id, name, marks in data:
        student = Student(student_id, name)

        for mark in marks:
            student.add_mark(mark)

        manager.add_student(student)

    manager.display_students()

    print("\nSearch Example")
    student = manager.find_student(3)

    if student:
        print(student)
    else:
        print("Student not found.")

    print(f"\nReport generated at {datetime.now()}")


if __name__ == "__main__":
    main()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=800,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[1])