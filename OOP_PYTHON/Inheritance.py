# Python Practice Repository
# Topic : Inheritance
# Author : Rana Umar Draz
# Defication : Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and behaviors (methods) from another class. The class that inherits is called the child class or subclass, while the class being inherited from is called the parent class or superclass. Inheritance promotes code reusability and establishes a hierarchical relationship between classes. In this example, we define a Person class as the parent class with attributes name and city, and a Student class as the child class that inherits from Person and adds an additional attribute department. The Student class can access the attributes and methods of the Person class using the super() function.
# Using inheritance, we can create instances of the Student class that have access to both the attributes and methods of the Person class, as well as their own unique attributes and methods. This allows us to model real-world relationships between different entities in a more organized and efficient manner.

class Person:

    def __init__(self, name, city):

        self.name = name
        self.city = city

    def display_person(self):

        print("=" * 50)
        print("PERSON INFORMATION")
        print("=" * 50)
        print("Name :", self.name)
        print("City :", self.city)

class Student(Person):

    def __init__(self, name, city, department):

        super().__init__(name, city)

        self.department = department

    def display_student(self):

        self.display_person()

        print("Department :", self.department)

student = Student(
    "Rana Umar Draz",
    "Faisalabad",
    "Software Engineering"
)

student.display_student()