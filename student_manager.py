from student import Student
from file_handler import load_students, save_students


class StudentManager:

    def __init__(self):
        self.students = []

        data = load_students()

        for item in data:
            self.students.append(Student.from_dict(item))

    def save(self):
        save_students([student.to_dict() for student in self.students])

    def add_student(self):

        student_id = input("Enter Student ID : ")

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter Name : ")
        age = input("Enter Age : ")
        course = input("Enter Course : ")

        student = Student(student_id, name, age, course)

        self.students.append(student)

        self.save()

        print("Student Added Successfully.")

    def display_students(self):

        if len(self.students) == 0:
            print("No Student Found.")
            return

        print("\nStudent Records\n")

        for student in self.students:
            print("----------------------------")
            print("ID :", student.student_id)
            print("Name :", student.name)
            print("Age :", student.age)
            print("Course :", student.course)

    def search_student(self):

        student_id = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found\n")

                print("ID :", student.student_id)
                print("Name :", student.name)
                print("Age :", student.age)
                print("Course :", student.course)

                return

        print("Student Not Found.")

    def update_student(self):

        student_id = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == student_id:

                student.name = input("Enter New Name : ")
                student.age = input("Enter New Age : ")
                student.course = input("Enter New Course : ")

                self.save()

                print("Student Updated Successfully.")

                return

        print("Student Not Found.")

    def delete_student(self):

        student_id = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                self.save()

                print("Student Deleted Successfully.")

                return

        print("Student Not Found.")