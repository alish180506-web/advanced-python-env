import math

for i in range(1, 4):
    arr = [int(x) for x in input(f"Massive {i} by space: ").split()]
    s = sum(arr)
    m = s / len(arr) if len(arr) > 0 else 0
    print(f"Massive {i}: Sum = {s}, average = {m}")