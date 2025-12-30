x, y, z, t = map(float, input("Enter sides X Y Z T: ").split())
diag = (x**2 + y**2)**0.5
p = (z + t + diag) / 2
area2 = (p * (p-z) * (p-t) * (p-diag))**0.5
print("Area:", (0.5 * x * y) + area2)