<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:a855f7&height=200&section=header&text=OOP%20in%20Python&fontSize=45&fontColor=ffffff&fontAlignY=38&desc=Mastering%20Object-Oriented%20Programming%20%7C%20Clean%20Code%20%7C%20Software%20Design&descAlignY=58&descSize=15" />

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=20&pause=1000&color=6366f1&center=true&vCenter=true&width=750&lines=🏗️+Object-Oriented+Programming+in+Python;🔒+Encapsulation+%7C+Abstraction+%7C+Inheritance;🔄+Polymorphism+%7C+Clean+Code+%7C+Design+Principles;🚀+Building+Professional+Software+Engineering+Skills" />

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![OOP](https://img.shields.io/badge/Object--Oriented-Programming-6366f1?style=for-the-badge&logo=academia&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)
![Pillars](https://img.shields.io/badge/4%20Pillars-Mastered-a855f7?style=for-the-badge&logo=buffer&logoColor=white)
![GitHub](https://img.shields.io/badge/Open%20Source-Portfolio-1f2937?style=for-the-badge&logo=github&logoColor=white)

<br/>

> *"Good software begins with good design. Good design begins with OOP."*

</div>

---

## 🧭 About This Repository

Welcome to my **Object-Oriented Programming (OOP) in Python** repository — a structured, concept-driven practice journal built to master the **4 Pillars of OOP** through clean code, real examples, and hands-on exercises.

This repository is not just theory. Every concept is implemented through practical Python code, designed to build the **software engineering mindset** required for real-world development, technical interviews, and advanced AI/ML engineering.

> Every class designed here = one step closer to professional software engineering. 🚀

---

## 🎯 Objectives

```python
objectives = [
    "Master the 4 Pillars of OOP",
    "Design modular and reusable code",
    "Understand class relationships and object behavior",
    "Write clean, maintainable, professional code",
    "Prepare for technical interviews",
    "Build a strong base for advanced software development",
]
```

---

## 📚 Topics Covered

<div align="center">

| # | 📁 Topic | 🔍 What's Inside |
|:---:|:---|:---|
| 01 | 🏛️ **Intro to OOP** | What is OOP, Why OOP, Procedural vs OOP |
| 02 | 🧩 **Classes & Objects** | Creating Classes, Objects, Instance Variables, Methods |
| 03 | ⚙️ **Constructors** | `__init__()`, Default, Parameterized Constructors |
| 04 | 🔒 **Encapsulation** | Data Hiding, Getters, Setters, Access Control |
| 05 | 🎭 **Abstraction** | Abstract Classes, Abstract Methods, `abc` Module |
| 06 | 🧬 **Inheritance** | Single, Multiple, Multilevel, Hierarchical, Hybrid |
| 07 | 🔄 **Polymorphism** | Method Overriding, Duck Typing, Overloading Concept |
| 08 | 🔐 **Access Modifiers** | Public, Protected, Private Members |

</div>

---

## 🏛️ The 4 Pillars of OOP

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║              4 PILLARS OF OBJECT-ORIENTED PROGRAMMING    ║
╠══════════════╦═══════════════╦══════════════╦════════════╣
║  🔒           ║  🎭           ║  🧬          ║  🔄        ║
║ ENCAPSULATION ║  ABSTRACTION  ║  INHERITANCE ║POLYMORPHISM║
║               ║               ║              ║            ║
║ Protect data  ║ Hide complex  ║ Reuse code   ║ One action ║
║ inside class  ║ implementation║ from parent  ║ many forms ║
╚══════════════╩═══════════════╩══════════════╩════════════╝
```

</div>

---

## 🗂️ Repository Structure

```
📦 OOP_PYTHON/
│
├── 📁 Classes_Objects/
│     └── classes_objects.py
│
├── 📁 Constructors/
│     └── constructors.py
│
├── 📁 Encapsulation/
│     └── encapsulation.py
│
├── 📁 Abstraction/
│     └── abstraction.py
│
├── 📁 Inheritance/
│     └── inheritance.py
│
├── 📁 Polymorphism/
│     └── polymorphism.py
│
├── 📁 Access_Modifiers/
│     └── access_modifiers.py
│
└── 📁 Practice_Exercises/
      └── exercises.py
```

---

## 🚀 Getting Started

```bash
# Step 1 — Clone the repository
git clone https://github.com/ranaumar9276-umar/OOP_PYTHON.git

# Step 2 — Navigate to any topic
cd OOP_PYTHON/Inheritance

# Step 3 — Run any file
python inheritance.py
```

> ✅ No external libraries needed — **Pure Python only!**

---

## 💡 Code Snippets Preview

<details>
<summary>🧩 <b>Classes & Objects</b></summary>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! I'm {self.name}, {self.age} years old.")

s1 = Student("Rana Umar", 21)
s1.introduce()
# Output: Hi! I'm Rana Umar, 21 years old.
```
</details>

<details>
<summary>🔒 <b>Encapsulation</b></summary>

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

account = BankAccount(5000)
account.deposit(1000)
print(account.get_balance())  # Output: 6000 ✅
```
</details>

<details>
<summary>🧬 <b>Inheritance</b></summary>

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof! 🐕")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow! 🐱")

d = Dog()
d.speak()  # Output: Dog says: Woof! 🐕
```
</details>

<details>
<summary>🔄 <b>Polymorphism</b></summary>

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):
    def area(self):
        return 10 * 4

shapes = [Circle(), Rectangle()]
for shape in shapes:
    print(f"Area: {shape.area()}")
# Output: Area: 78.5 | Area: 40 ✅
```
</details>

<details>
<summary>🎭 <b>Abstraction</b></summary>

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started 🚗")

c = Car()
c.start_engine()  # Output: Car engine started 🚗
```
</details>

---

## 📈 Recommended Learning Path

```
🟢 Start Here
│
├── 01 → Intro to OOP (Why OOP?)
├── 02 → Classes & Objects
├── 03 → Constructors (__init__)
├── 04 → Access Modifiers
├── 05 → Encapsulation 🔒
├── 06 → Abstraction 🎭
├── 07 → Inheritance 🧬
└── 08 → Polymorphism 🔄
             │
             ▼
    🏁 OOP in Python — COMPLETE ✅
             │
             ▼
    🚀 Ready for Advanced Python & Software Design
```

---

## 🧠 Skills Developed

<div align="center">

| Skill | Level |
|:---|:---|
| Class Design | ✅ Mastered |
| Encapsulation | ✅ Mastered |
| Abstraction | ✅ Mastered |
| Inheritance (All Types) | ✅ Mastered |
| Polymorphism | ✅ Mastered |
| Access Modifiers | ✅ Mastered |
| Code Reusability | ✅ Mastered |
| Modular Programming | ✅ Mastered |

</div>

---

## 🔮 What's Next After OOP?

```
✅ OOP in Python (This Repo)
         ↓
📦 Python Advanced — Decorators, Generators, Iterators
         ↓
📊 NumPy & Pandas (Data Science)
         ↓
🤖 Scikit-Learn & Machine Learning
         ↓
🧠 Deep Learning & Neural Networks
         ↓
🚀 AI Engineering & Real-World Projects
```

---

## 🛠️ Tools & Technologies

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=FFD43B)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

</div>

---

## 👨‍💻 About Me

**Rana Umar Draz**
Software Engineering Student | Future ML Engineer | Future Data Scientist

I believe that mastering **Object-Oriented Programming** is one of the most critical steps toward becoming a professional software engineer capable of building scalable, intelligent systems.

> *"Master the fundamentals. Everything advanced is just fundamentals applied creatively."*

---

## 🌐 Connect With Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-ranaumar9276--umar-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ranaumar9276-umar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rana%20Umar%20Draz-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rana-umar-draz-95951733b)

</div>

---

<div align="center">

### ⭐ If this repository helped you, please give it a Star!

*Your support keeps me motivated to keep learning and sharing.* 🙏

<br/>

**🔥 Design • Code • Practice • Refactor • Repeat 🔥**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:a855f7,100:6366f1&height=120&section=footer" />

</div>
