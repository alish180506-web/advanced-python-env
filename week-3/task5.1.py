def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

a, b, c, d = map(int, input("A, B, C, D for (A/B - C/D): ").split())
num = a * d - c * b
den = b * d
common = get_gcd(num, den)
print(f"Result: {num//common}/{den//common}")