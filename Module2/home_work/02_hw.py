# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

n=int(input("Количество коров: "))
if 5<=n%10<=9 or 11<=n%100<=19 or n%10==0:
    print("На лугу пасется", n, "коров.")
elif n%10==1:
    print("На лугу пасется", n, "корова.")
elif 2<=n%10<=4:
    print("На лугу пасется", n, "коровы.")
