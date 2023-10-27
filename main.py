class Person:
    def __init__(self, name, age):
        self.name = name
        self.hapiness = 100
        self.age = age
        self.money = 1000
class Student(Person):
   def __init__(self):
       def __init__(self):
            super().__init__()
   def rest(self):
        self.hapiness += 10
student = Student('Bob')
student1 = Student('Jack')
student.rest()
student1.rest()
print(student.name, student.hapiness)


class Worker:
    def __init__(self):
        super().__init__()
    def rest(self):
        self.money += 5000