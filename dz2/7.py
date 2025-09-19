a = list(map(int, input().split(" ")))
max_count = 0
max_element = None

for el in a:
    count = 0
    for el1 in a:
        if el == el1:
            count += 1
    if count > max_count:
        max_count = count
        max_element = el

print(max_element)
