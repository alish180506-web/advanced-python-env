s = input()

if s[0] == 'x':
    x = int(s[4]) - int(s[2])
elif s[2] == 'x':
    if s[1] == '+':
        x = int(s[4]) - int(s[0])
    else:
        x = int(s[0]) - int(s[4])
else:
    x = int(s[0])
    if s[1] == '+':
        x = int(s[4]) - x
    else:
        x = x - int(s[4])

print(x)
