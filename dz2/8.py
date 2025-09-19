N = int(input())
a = list(map(int, input().split(" ")))

max_trans = float("inf")
min_trans = float("-inf")

for i in range(N//2 + 1):
    max_el = float("-inf")
    min_el = float("inf")
    for el in a:
        if el > max_el and el < max_trans:
            max_el = el
        if el < min_el and el > min_trans:
            min_el = el
    max_trans = max_el
    min_trans = min_el

if min_trans == max_trans:
    print(min_trans)

