s = [float(x) for x in input("Enter 4 sides and diagonal: ").split()]
def tri_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p-a) * (p-b) * (p-c))**0.5

area = tri_area(s[0], s[1], s[4]) + tri_area(s[2], s[3], s[4])
print("Total Area:", area)