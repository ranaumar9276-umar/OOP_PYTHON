# Python Practice Repository
# Topic : Class & Object
# Author : Rana Umar Draz
# Description : Student Information System
# Definition of Class Student with a method to display student information using print statements.
# Class is a blueprint for creating objects. An object is an instance of a class. In this case, the Student class represents a student and has a method to display the student's information.
# Objects are created from the class and can access its methods and attributes. In this example, we create an object student1 of the Student class and call the display method to print the student's information.

class Student:

    def display(self):

        print("=" * 50)
        print("STUDENT PROFILE")
        print("=" * 50)
        print("Name       : Rana Umar Draz")
        print("University : Superior University")
        print("Department : Software Engineering")
        print("Semester   : 6")
        print("Goal       : AI / ML Engineer")

student1 = Student()

student1.display()