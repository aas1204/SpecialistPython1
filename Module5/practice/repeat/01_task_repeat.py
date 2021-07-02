# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of=-5, to=5):
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(of, to))
    return result_list

my_list = gen_list(10)

print(my_list)
