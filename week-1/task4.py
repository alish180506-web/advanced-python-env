# task4.py

try:
   
    N = int(input("Enter an integer N: "))
    sum_of_numbers = (N * (N + 1)) // 2

    print(sum_of_numbers)

except ValueError:
    print("Error: Please enter a valid integer.")
