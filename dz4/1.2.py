from vector1 import Vector
def vector_multiplication(self, other):
    if isinstance(other, Vector):
        return Vector(self.y*other.z - self.z*other.y, -self.x*other.z + self.z*other.x, self.x*other.y - self.y*other.x)
    else:
        raise ValueError
print("Введите вектора координат множества точек в формате {x, y}")
print("Для прекращения ввода оставте поле пустым и нажмите Enter")
last = input()
vectors = []
while last != "":
    vectors.append(Vector(last))
    last = input()

n = 0
A = -float("inf")
for i in vectors:
    for j in vectors:
        if i == j:
            continue
        for k in vectors:
            area = 0.5*abs(vector_multiplication(((-1)*i + j), ((-1)*i + k)))
            if area >= A:
                A = area
print(A)