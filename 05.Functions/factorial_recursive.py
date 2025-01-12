def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

def main():
    number = 5
    result = fact(number)
    print(result)
    return result

main()