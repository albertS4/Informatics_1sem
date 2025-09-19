sym = "AHIMOTUVWXY18"
mir = {"E":"3", "3":"E", "J":"L", "L":"J", "S":"2", "2":"S", "Z":"5", "5":"Z"}

s = input()

palindrome = False
if s == s[::-1]:
    palindrome = True

mirrored = True

s1 = ""
for i in s:
    if not((i in sym) or i in mir.keys()):
        mirrored = False
        break
    elif i in sym:
        s1 += i
    else:
        s1 += mir[i]

if s1[::-1] != s:
    mirrored = False

if not palindrome and not mirrored:
    print(s, "is not a palindrome.")
elif palindrome and not mirrored:
    print(s, "is a regular palindrome.")
elif not palindrome and mirrored:
    print(s, "is a mirrored string.")
elif palindrome and mirrored:
    print(s, "is a mirrored palindrome.")
