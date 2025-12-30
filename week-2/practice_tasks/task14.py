text = input()

for word in text.split():
    if word.startswith("a") or word.endswith("i"):
        print(word)
