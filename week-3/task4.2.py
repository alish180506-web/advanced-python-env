ca, cb, r = map(float, input("x, y and R: ").split())
count = 0
for p in ['P', 'F', 'L']:
    px, py = map(float, input(f"Point {p} (x y): ").split())
    if (px-ca)**2 + (py-cb)**2 <= r**2: count += 1
print("Points inside:", count)