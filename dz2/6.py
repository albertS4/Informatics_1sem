a = list(map(int, input().split(" ")))

for i in range(len(a)):
    repeats = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            repeats += 1
        
    if repeats == 1:
        print(a[i], end = " ")
        

