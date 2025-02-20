#ІТЕРАТОРИ
# my_list = [1, 2, 3]
# iterator = iter(my_list) #процес ітерації
#
# for elem in iterator: #одноразовий об'кт
#     print(elem)

# print(next(iterator)) #наступна ітерація
# print(next(iterator))
# print(next(iterator))

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i  > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# for elem in count:
#     print((elem))
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(iter(count))
# print(next(count))

#ГЕНЕРАТОРИ

# def reise_to_the_degrees(number):
#     i = 0
#     # for _ in range (max_degree):
#     while True:
#         # yield number **i #повернення результату ітерації
#         # i += 1
#         result = number**1
#         yield result
#         if result > 100**20:
#             return
#         i+=1
#
# res = reise_to_the_degrees(122345)
# print(res)
# for _ in res:
#     print(_)

# class Helper:
#     def __init__(self, work):
#         self.work = work
#
#     def __call__(self, work): #виклик об'єкта
#         return f"I will help you with {self.work}. Afterwards I will help you with {work}"
# helper = Helper("homework")
# print(helper("cleaning"))

# :
#     work_in_memodef helper(work)ry = work
#
#     def helper(work):
# #         return f"I will help you with {work_in_memory}. Afterwards I will help you with {work}"
# #     return helper
# # helper = helper("homework")
# # print(helper("cleaning"))
# # print(helper("driving"))


# words = ["apple", "banana", "orange", "computer", "table"]
# iterator = iter(words)
# for word in iter(words):
#     print(f"{word}: {len(word)} letters.")

# def power_of_three():
#     for i in range(21):
#         yield f"3 в {i}-му степені = {3 ** i}"
#
# for res in power_of_three():
#     print(res)


#ДЕКОРАТОРИ

# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             results = function(*args, **kwargs)
#         except Exception as exc:
#             print(f"We have problems {exc}")
#         else:
#             print(f"No problems. Result - {results}")
#     return checker()
#
# @checker
# def calculate(expression):
#     return eval(expression) #допоміжна функція
# # calculate = checker(calculate)
# calculate("2+2")

# def checker(*exc_types):
#     def checker(function):
#         def checker(*args, **kwargs):
#             try:
#                 results = function(*args, **kwargs)
#             except exc_types as exc:
#                 print(f"We have problems {exc}")
#             else:
#                 print(f"No problems. Result - {results}")
#         return checker
#     return checker
#
# @checker (NameError, TypeError, SyntaxError)
# def calculate(expression):
#     return eval(expression) #допоміжна функція
# # calculate = checker(calculate)
# calculate("2+28")

def sum():
    total =[0]
    def update_total(x):
        total[0] += x
    def get_total():
        return total[0]
    return update_total, get_total
add_to_sum, current_sum = sum()

add_to_sum(5)
add_to_sum(3)
add_to_sum(9)
print(current_sum())