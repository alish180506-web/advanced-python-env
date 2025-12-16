# task3.py

try:
    A = float(input("Enter a real number A (e.g., 12.34): "))

    integer_part = int(A)

    fractional_part_raw = A - integer_part
    new_integer_part = round(fractional_part_raw * 100)
    new_fractional_part = integer_part / 100
    new_number = new_integer_part + new_fractional_part

    print(f"{new_number:.2f}") 

except ValueError:
    print("Error: Please enter a valid number.")
