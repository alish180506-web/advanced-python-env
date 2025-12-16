# task5.py

try:
    result = float(input("Enter the final result after all actions: "))

    step1 = result / 2
    step2 = step1 - 8
    intended_number = step2 / 5

    print(f"The intended number was: {intended_number}")

except ValueError:
    print("Error: Please enter a valid number.")