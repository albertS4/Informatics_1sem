import math
numbers = list(map(float, input().split(" ")))

product = 1
for n in numbers:
    product = product*n

print(math.pow(product, 1/len(numbers)))
