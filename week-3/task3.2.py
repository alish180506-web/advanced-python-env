text = input("String: ")
words = text.split()
sorted_words = ["".join(sorted(w)) for w in words]
print("Result:", " ".join(sorted_words))