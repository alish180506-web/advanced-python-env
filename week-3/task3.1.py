def get_hypo(a, b):
    return (a**2 + b**2)**0.5

a1, b1 = map(float, input("A: ").split())
a2, b2 = map(float, input("B: ").split())

h1 = get_hypo(a1, b1)
h2 = get_hypo(a2, b2)

print(f"C: {h1} и {h2}")
if h1 > h2:
    print("First biger")
elif h2 > h1:
    print("Second biger")
else:
    print("They are same")