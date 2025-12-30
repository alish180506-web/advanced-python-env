n = int(input("Enter n: "))
for i in range(1, n + 1):
    digits = str(i)
    if '0' not in digits and all(i % int(d) == 0 for d in digits):
        print(i, end=" ")