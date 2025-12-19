# task9.py

ticket_number = input("Enter the six-digit ticket number: ")

if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Error: The ticket number must be a six-digit number.")

else:
    sum_first_three = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])

    sum_last_three = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

    if sum_first_three == sum_last_three:
        print("YES")
    else:
        print("NO")