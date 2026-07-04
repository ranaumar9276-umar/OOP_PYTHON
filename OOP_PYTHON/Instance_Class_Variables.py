# Topic : Instance & Class Variables
# Instance variables are unique to each instance of a class, while class variables are shared among all instances of the class. In this example, we define a class variable university that is shared by all instances of the Student class. Each student instance has its own name and skill attributes, which are instance variables. The display method prints the student's information along with the shared university name.
# Variables defined inside the constructor (__init__) are instance variables, while variables defined outside the constructor but inside the class are class variables. In this example, university is a class variable, while name and skill are instance variables.

class Student:

    university = "Superior University"

    def __init__(self, name, skill):

        self.name = name
        self.skill = skill

    def display(self):

        print("=" * 40)
        print("Name :", self.name)
        print("Skill :", self.skill)
        print("University :", Student.university)

student1 = Student("Rana Umar", "Machine Learning")
student2 = Student("Ali", "Flutter")
student1.display()
student2.display()

print()
print("Class Variable")

print(Student.university)