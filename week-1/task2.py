# task2.py

try:
    salaries_str = input("Enter three salaries ( 100 500 1000): ")
    salaries_list = list(map(int, salaries_str.split()))

    if len(salaries_list) != 3:
        raise ValueError("Please enter exactly three salaries.")

    max_salary = max(salaries_list)
    min_salary = min(salaries_list)

    difference = max_salary - min_salary
    print(difference)

except ValueError as e:
    print(f"Error: {e}")