with open("input.txt", "r") as f:
    text = f.read()

last_c = ""
sent = 0

special_symbols = ".!?"

for c in text:
    if c in special_symbols and not (last_c in special_symbols):
        sent += 1
    last_c = c

if not (last_c in special_symbols):
    sent += 1

print(sent)
