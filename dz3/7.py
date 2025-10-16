import string

words = {}

data = ""
with open("7.txt", "r") as f:
    data = f.read()

for c in string.punctuation:
    data = data.replace(c, " ")

data = data.lower()
data = filter(lambda x: x != " " and x != "" , data.split(" "))

for d in data:
    if d in words:
        words[d] += 1
    else:
        words[d] = 1

max_key = None
max_value = 0
for w in words:
    if words[w] > max_value:
        max_value = words[w]
        max_key = w
print(max_key, words[max_key])
