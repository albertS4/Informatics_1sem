with open("input.txt", "r") as f:
    numbers = list(map(int, f.readline().split(" ")))
    operations = list(f.readline().split(" "))
print(numbers)
print(operations)

Ns = [numbers[0]]
Os = []

for i in range(1, len(numbers)):
    if operations[i - 1] == "*":
        Ns[-1] = Ns[-1]*numbers[i]
    else:
        Ns.append(numbers[i])
        Os.append(operations[i - 1])

print(Ns)
print(Os)

total = Ns[0]
for i in range(1, len(Ns)):
    if Os[i - 1] == "-":
        total -= Ns[i]
    elif Os[i - 1] == "+":
        total += Ns[i]

print(total)
