import math

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("A: "))
b = int(input("B: "))
gcd_val = get_gcd(a, b)
lcm_val = (a * b) // gcd_val
print(f"GCD: {gcd_val}, LCM: {lcm_val}")