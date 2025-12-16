# task6.py

try:
    num1 = float(input("First number: "))
    operation = input("Operation (+, -, *, /): ")
    num2 = float(input("Second number: "))
    
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Error: Unknown operation.")

    if result is not None:
        print(f"Result: {num1} {operation} {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
