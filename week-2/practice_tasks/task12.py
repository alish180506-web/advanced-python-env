text = input()

for word in text.split():
    if word.endswith("I"):
        print(word)
