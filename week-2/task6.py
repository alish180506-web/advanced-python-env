def all_eq(lst):
    max_len = max(len(s) for s in lst)
    return [s + " " * (max_len - len(s)) for s in lst]

# ДОБАВЬТЕ ЭТИ СТРОКИ:
data = ["apple", "banana", "kiwi"]
print(all_eq(data))