# Даны два целые числа a и b. Выведите на экран все целые четные числа от a до b включительно.
# Формат входных данных: Дано два целых числа a и b. Гарантируется, что a < b
# Формат выходных данных: Выведите все числа, требуемые по условию задачи.

a=int(input("Введите число a: "))
b=int(input("Введите число b (должно соблюдаться условие b>a): "))
while a<=b:
    if a%2==0:
        print(a)
    a += 1
