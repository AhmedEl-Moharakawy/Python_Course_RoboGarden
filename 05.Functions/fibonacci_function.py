def fibonacci_fun(n):
    if n <= 1:
        return n
    else:
        return fibonacci_fun(n-1) + fibonacci_fun(n-2)

def main():
    n = 9
    result = fibonacci_fun(n)
    print(result)

main()