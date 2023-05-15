def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x - 1)


def factorial(n):
    res = 1
    if n == 0 or n == 1:
        return res
    for i in range(2, n + 1):
        res *= i
    return res


if __name__ == '__main__':
    num = 5
    print(fact(num))
    print(factorial(num))
