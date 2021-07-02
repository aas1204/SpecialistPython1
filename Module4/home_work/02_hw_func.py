# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

a=(12, 10)
b=(14, 10)
c=(10, 12)
ab=distance(*a, *b)
bc=distance(*b, *c)
ac=distance(*a, *c)

def min_dist(*args):
    min_el=args[0]
    for el in args:
        if el<min_el:
            min_el=el
    return min_el


# TODO: your code here
print("Самый короткий отрезок:", min_dist(ab, bc, ac))
