s = input()

count = 0
for i in range(len(s)):
    part = s[i:i+5]
    if part == ">>-->" or part == "<--<<":
        count += 1

print(count)
