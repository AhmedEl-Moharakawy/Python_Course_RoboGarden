num = int(input("Enter the number of iterations: "))

for i in range(num):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        a, b = 0, 1
        for j in range(2, i+2):
            a, b = b, a + b
        print(b)