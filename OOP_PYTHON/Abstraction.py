# Topic : Abstraction


from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):

     pass

class AIEngineer(Employee):

    def salary(self):

        print("Monthly Salary : 350000 PKR")

class DataScientist(Employee):

    def salary(self):

        print("Monthly Salary : 400000 PKR")

engineer = AIEngineer()
scientist = DataScientist()
engineer.salary()
scientist.salary()