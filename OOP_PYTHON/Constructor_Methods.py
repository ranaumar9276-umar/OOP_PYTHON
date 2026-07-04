# Topic : Constructor (__init__)
# Constructor is a special method in Python classes that is automatically called when an object of the class is created. It is used to initialize the attributes of the object. The constructor method is defined using the __init__() method, and it can take parameters to set the initial values of the object's attributes. In this example, we define a Student class with a constructor that takes name, semester, and cgpa as parameters and initializes the corresponding instance variables. The show method is used to display the student's information.
# Variables defined inside the constructor (__init__) are instance variables, which are unique to each instance of the class. Each student instance has its own name, semester, and cgpa attributes, which are initialized using the constructor. The show method prints the student's information.


class Student:
    def __init__(self, name, semester, cgpa):

        self.name = name
        self.semester = semester
        self.cgpa = cgpa

    def show(self):

        print("=" * 40)
        print("Student :", self.name)
        print("Semester :", self.semester)
        print("CGPA :", self.cgpa)

student1 = Student("Rana Umar", 6, 3.72)
student2 = Student("Ali", 6, 3.55)
student1.show()
student2.show()