data = ["apple", "banana", "kiwi"]

max_len = 0
for s in data:
    if len(s) > max_len:
        max_len = len(s)

result = []
for s in data:
    result.append(s + "_" * (max_len - len(s)))

for word in result:
    print(f"'{word}'")
