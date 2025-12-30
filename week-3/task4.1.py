def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))

num = a * d
den = b * c
common = get_gcd(num, den)
print(f"Result: {num//common}/{den//common}")