def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


def sum_array_2(arr):
    total = 0
    for x in arr:
        total += x
    return total


if __name__ == '__main__':
    print(sum_array([11, 22, 33]))
    print(sum_array_2([11, 22, 33]))
