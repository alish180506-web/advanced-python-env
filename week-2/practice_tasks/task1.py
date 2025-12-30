text = input()

count = 0
for word in text.split():
    if word.lower().startswith("е"):
        count += 1

print(count)
