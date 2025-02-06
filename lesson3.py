# git - перевіряє чи встановлений гід
# git init - порожня папка в гіт
# git add . - додає всі файли папки у гіт
# git comit -m "назва" - завантаження редагованого коду(там де назва будь що)
# git -M main + - додати гілку меін
# git remote add origin ... - зв'язати локальний репозиторій з гіт
# git pussh -u origin main - авантажити проект в гіт

# class Student:
#     print("Hello")
#     def __init__(self): # конструктор класу
#         self.height = 160
#         print(self)
# first_student = Student()
# Student.__init__(self = first_student)

# class Student:
#     def __init__(self, height = 160): # конструктор класу
#         self.height = height
# nick = Student()
# kate = Student(height = 170)
# print(nick.height)
# print(kate.height)



# class Student:
#     amount_of_student = 0 # атрибут класу
#     def __init__(self, height = 160): # конструктор класу
#         self.height = height
#         Student.amount_of_student +=1
# nick = Student()
# kate = Student(height = 170)
# print(nick.amount_of_student)
# print(kate.amount_of_student)


# class Student:
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()


#МЕТОДИ

# class Student:
#     amount_of_student = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_student+=1
#     def grow(self, height=1): #метод
#         self.height+=height
# nick=Student()
# kate=Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

if self.food <= 0
    self.shopping()
else:
    gladness

# import random
# class Student:
#     def __init__(self, name):
#         self.name = name #ім'я
#         self.gladness = 50 #радість
#         self.progress = 0 #прогрес у навчанні
#         self.alive = True #перевірка життя студента
#
#     def to_study(self): #навчання
#         print("Time to study")
#         self.progress += 0.12
#         self.gladness -= 3
#
#     def to_chill(self): #відпочинок
#         print("Rest time")
#         self.gladness += 5
#         self.progress -= 0.1
#
#     def to_sleep(self): #сон
#         print("I will sleep")
#         self.gladness += 3
#
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("Cast out...")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depression...")
#             self.alive = False
#         elif self.progress > 5:
#             print("Passed externally...")
#             self.alive = False
#
#     def end_of_day(self):
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#
#     def live(self, day):
#         day = "Day" + str(day) + "of" + self.name + "life"
#         print(f"{day:=^50}")
#         live_cube = random.randint(1,3)
#         if live_cube ==1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
# nick = Student(name = "Nick")
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)


class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount} UAH. Balance: {self.balance} UAH")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You haven't enough money!")
        else:
            self.balance -= amount
            print(f"Removed: {amount} UAH. Balance: {self.balance} UAH.")

accout = BankAccount("12345", 1000)
accout.deposit(500)
accout.withdraw(300)
accout.withdraw(1500)