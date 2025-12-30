
number = int(input("Enter number: "))
octal_value = oct(number)[2:]
octal_code = octal_value.zfill(10)

print("10-digit octal code:", octal_code)