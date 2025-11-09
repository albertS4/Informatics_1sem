from vector1 import Vector
print("Введите вектора координат множества точек в формате {x, y}")
print("Для прекращения ввода оставте поле пустым и нажмите Enter")
last = input()
total_vector = Vector(0, 0)
number = 0
while last != "":
    v = Vector(last)
    total_vector += v
    number += 1
    last = input()

print(total_vector*(1/number))