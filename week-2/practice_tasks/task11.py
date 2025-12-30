text = input()
text = text.replace("!", ".")

max_n = 0
current = 0

for ch in text:
    if ch == "n":
        current += 1
        if current > max_n:
            max_n = current
    else:
        current = 0

print(text)
print(max_n)
