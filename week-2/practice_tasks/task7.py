text = input()
half = len(text) // 2

result = ""
for i in range(len(text)):
    if i < half and text[i] == "n":
        result += "*"
    else:
        result += text[i]

print(result)
