import random

random.seed(99)

letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
with open("prestuplenie-i-nakazanie.txt", "r", encoding = "utf-8") as f:
    text = f.read().lower()

words = []
last_word = ""
for i in text:
    if "." == i:
        words.append(last_word)
        words.append(".")
        last_word = ""
        continue
    if i in letters:
        last_word += i
    elif last_word != "":
        words.append(last_word)
        last_word = ""

with open("pi.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(words))

markoff = {}

for i in range(1, len(words)):
    if not(words[i - 1] in markoff):
        markoff.update({words[i - 1]: {words[i]: 1}})
    elif not(words[i] in markoff[words[i - 1]].keys()):
        markoff[words[i - 1]].update({words[i]: 1})
    else:
        markoff[words[i - 1]][words[i]] += 1
def generate(w, minimal = 5, maximal = 1000):
    if not w in markoff:
        print(">>>Нет слова", w)
        return [w]
    a = [w]
    i = 0
    for i in range(maximal):
        if a[-1] == "." and i >= minimal:
            break
        l = markoff[a[-1]]
        its = list(l.items())
        m = sum(sorted(list(l.values()))[-5:])/5
        random.shuffle(its)
        for it in its:
            if it[1] >= 0.75*m:
                if it[0] == "." and i < minimal:
                    continue
                a.append(it[0])
                if i < minimal:
                    i += 1
    return a

print(*generate("однажды"))
#print(*generate("поникнувшись"))
print(*generate("утро"))
#print(*generate("лужин"))
            
    
