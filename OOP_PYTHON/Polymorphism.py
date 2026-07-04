# Topic : Polymorphism

class PythonDeveloper:
    def work(self):
        print("Developing AI applications using Python")
class FlutterDeveloper:
    def work(self):
        print("Developing Android applications using Flutter")
class WebDeveloper:
    def work(self):
        print("Developing Full Stack Web Applications")

developers = [
    PythonDeveloper(),

    FlutterDeveloper(),

    WebDeveloper()

]
for developer in developers:

    developer.work()