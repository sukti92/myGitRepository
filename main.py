class Human():
    country = 'Bangladesh'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name:{self.name} Age:{self.age}")

    def __str__(self):
        return f"Name:{self.name} Age:{self.age}"

class Student(Human):
    def __init__(self, name, age, cgpa, studentid):
        Human.__init__(self, name, age)
        self.cgpa = cgpa
        self.studentid = studentid

    def display(self):
        super().display()
        print(f"ID:{self.studentid} CGPA:{self.cgpa}")

    def __str__(self):
        return f"Name:{self.name} ID:{self.studentid} CGPA:{self.cgpa} Age:{self.age}"


human = Human("abc", 21)
print(human)
'''
human1 = Human("bbb",22)
human1.country = "HHH"
print(human1.country)
print(human1.__class__.country)
print(human.country)
print(Human.country)
'''
student1 = Student('xx', 23, 3.5, '124')
print(student1)




