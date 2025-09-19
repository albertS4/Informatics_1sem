vowels = "аеёиоуыэюя"
cons = "бвгджзклмнпрстфхцчшщ"

with open("input.txt", "r", encoding = "utf-8") as f:
    text = f.read()

new_text = ""

for i in range(len(text)):
    new_text += text[i]
    if text[i] in vowels and (i == 0 or text[i - 1] in cons):
        new_text += "c" + text[i]

print(new_text)
