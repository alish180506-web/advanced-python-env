print("\n--- Array Swap ---")
m = int(input("Array length: "))
A = [int(input(f"Element {i}: ")) for i in range(m)]
print("Original:", A)
if m > 1: A[0], A[-1] = A[-1], A[0]
print("Result:", A)