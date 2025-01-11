first_number = float(input())
second_number = float(input())
sum = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
print(sum)
print(subtraction)
print(multiplication)

if second_number != 0:
    division = first_number / second_number
    print(division)
else: 
    print("Division by zero is not allowed")