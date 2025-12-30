import math

for i in range(1, 4):
    w, h = map(float, input(f"w {i}: ").split())
    print(f"S {i}:", w * h)