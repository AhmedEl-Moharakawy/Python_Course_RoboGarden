num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Invalid: negative numbers are not allowed")
elif num == 0:
    print(1)
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
