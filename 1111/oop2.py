'''class Human: #просте успадкування
    height = 170
    salary = 0
class Student(Human):
    height = 150
class Worker(Human):
    salary = 500
nick = Student()
ann = Worker()
print(nick.height, "cm")
print(nick.salary, "$")
print(ann.height, "cm")
print(ann.salary, "$")'''

'''class Grandparent: #ієархічне успадкування
     height = 170
     satiety = 100
     age = 60
class Parent(Grandparent):
     age = 40
class Child(Parent):
     height = 50
     def __init__(self):
         print(self.height, "cm")
         print(self.satiety, "pt")
         print(self.age, "years")
nick = Child()'''

'''class Hello:
    def __init__(self):
        print("Hello!")
class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")
x1 = Hello_World()'''

'''class Grandparent:
     def about(self):
        print("I am GrandParent")
     def about_myself(self):
        print("I am Grandparent")
class Parent(Grandparent):
     def about_myself(self):
        print("I am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

nick1 = Grandparent()
nick2 = Parent()
nick3 = Child()'''
class Computer:  #множинне успадкування

    def calculate(self):
        print("Calculating…")
    def __init__(self):
        super().__init__()
        self.memory = 128
class Display:
    def display(self):
        print("I display the image on the screen…")
    def __init__(self):
        super().__init__()
        self.resolution = "4k"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone()
iphone.calculate()
iphone.display()
iphone.print_info()

