import math

def triangle_area(side):
    return (math.sqrt(3) / 4) * side**2

a = float(input("A: "))
hexagon_area = 6 * triangle_area(a)
print("S:", hexagon_area)