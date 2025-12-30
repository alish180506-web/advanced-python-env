text = input()

start = text.find("(")
end = text.find(")")

print(text[start + 1:end])
