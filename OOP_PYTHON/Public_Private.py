# Topic : Public Private Protected


class Student:

    def __init__(self):

        self.name = "Rana Umar"          # Public

        self._semester = 6               # Protected

        self.__cgpa = 3.72               # Private

    def show(self):

        print("Name :", self.name)

        print("Semester :", self._semester)

        print("CGPA :", self.__cgpa)

student = Student()
student.show()

print()
print(student.name)
print(student._semester)

# print(student.__cgpa)  # Error