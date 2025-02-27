#print("Hello Word")

#name = input()
#print(name)

#from turtle import *
#shape("turtle")
#done()

#незмінні:
# (числа(int - цілі // bool - логічні(1,0 / true, false // float - дробові)))
#рядок (string)
#кортежі - tuple
# frozenset

# змінні:
# список - list
# словник - dict
# множина - set


# variable = 0
# if variable ==True:
#     print("+")
# else:
#     print("-")

# variable = 1
# while variable < 5:
#     variable+=1
#     print(variable)

# for i in 3,4,5:
#     print(i)

# for i in range (1, 11, 3):
#     print(i)


import random
number = random.randint(1, 50)
attempts = 7

print("Вгадай число від 1 до 50. В тебе є 7 спроб.")

while attempts > 0:
    guess = int(input("Введи свій здогад: "))

    for _ in range(1):
        if guess == number:
            print("Вітаю, ти вгадав моє число!")
            attempts = 0
        elif guess < number:
            print("Число більше.")
        else:
            print("Число менше.")

    attempts -= 1
    if attempts > 0 and guess != number:
        print(f"Залишені спроби: {attempts}")

if attempts == 0 and guess != number:
    print(f"У тебе закінчились спроби. Моє чило було {number}.")


