# class Parent:
#     classmethod and atters
# class Chaild(Parent):
#         classmethod and atters

# class Human:
#     height = 170
#
# class Student(Human): #успадковування класу
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# nick = Student()
# ann = Worker()
# print(nick.satiety)

# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
# nick = Child()


# class Computer:
#     def __init__(self):
#         self.memory = 128
#
# class Display:
#     def __init__(self):
#         self.resolution = "4k"
#
# class SmartPhone(Display,Computer):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
# iphone = SmartPhone()
# iphone.print_info()

class Animal:
    age = 10
    weight = 3
    population = 5

class Rhino(Animal):
    age = 5

class Koala(Rhino):
    population = 3

    def __init__(self):
        print(self.age)
        print(self.weight)
        print(self.population)
nick = Child()
