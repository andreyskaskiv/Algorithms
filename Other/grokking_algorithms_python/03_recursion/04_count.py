def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])


def count2(arr):
    num = 0
    for i in range(0, len(arr)):
        num += 1
    return num


if __name__ == '__main__':
    print(count([6, 23, 6, 44, 99, 4, -10]))
    print(count2([6, 23, 6, 44, 99, 4, -10]))
