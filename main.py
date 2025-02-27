# # завдання 1
# class Car:
#     def __init__(self, make: str, model: str, year: int):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_info(self) -> str:
#         return f"{self.year} {self.model} {self.make}"
#     def __str__(self):
#         return self.get_info()
# car1 =Car("Ford", "Mustang", 2023)
# print(car1)
# # завдання 2
# import random
# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#
#     def get_info(self):
#         return f"{self.name}, {self.age} years old, {self.position}, {self.salary} UAH"
#
# class Department:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#
#     def remove_random_employee(self):
#         if self.employees:
#             removed = random.choice(self.employees)
#             self.employees.remove(removed)
#             print(f"Removed employee: {removed.get_info()}")
#
#     def add_random_employee(self):
#         random_names = ["Alex", "Natalie", "Dmitry", "Irene", "Andrew"]
#         random_positions = ["Manager", "Developer", "Analyst", "Designer"]
#         new_employee = Employee(
#             random.choice(random_names),
#             random.randint(22, 50),
#             random.choice(random_positions),
#             random.randint(20000, 50000)
#         )
#         self.add_employee(new_employee)
#         print(f"Added employee: {new_employee.get_info()}")
#
#     def get_total_salary(self):
#         return sum(emp.salary for emp in self.employees)
#
#     def list_employees(self):
#         return [emp.get_info() for emp in self.employees]
#
# dept = Department("IT")
#
# dept.add_employee(Employee("John", 30, "Developer", 30000))
# dept.add_employee(Employee("Maria", 25, "Tester", 25000))
# dept.add_employee(Employee("Oleg", 35, "Database Administrator", 28000))
#
# print("\nEmployees in the IT department:")
# for info in dept.list_employees():
#     print(info)
#
# dept.remove_random_employee()
#
# dept.add_random_employee()
#
# print("\nUpdated list of employees:")
# for info in dept.list_employees():
#     print(info)
#
# print("\nTotal department salary:", dept.get_total_salary(), "UAH")

# # завдання 3
# class Device:
#     def turn_on(self):
#         return "Device is turned on"
#     def turn_off(self):
#         return "Device is turned off"
# class Smartphone(Device):
#     def call(self, number):
#         return f"Call on {number}"
# class Laptop(Device):
#     def open(self):
#         return "Opened development enviroment"
# smartphone = Smartphone()
# print(smartphone.turn_on())
# print(smartphone.call("+380982528462"))
# laptop = Laptop()
# print(laptop.turn_on())
# print(laptop.open())

# завдання 4
import random

def random_letter_generator():
    letters = "abcdefghijklmnopqrstuvwsyzABCDEFGHIGKLMNOPQRSTUVWXYZ"
    while True:
        yield random.choice(letters)
gen = random_letter_generator()
for i in range(1):
    print(next(gen))
