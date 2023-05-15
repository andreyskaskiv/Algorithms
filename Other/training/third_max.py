def thrid_max(array):
    # array.sort()

    if len(array) < 3:
        return None
    elif array[0] == array[1] == array[2] and len(array) <= 3:
        return None
    elif array[0] == array[1] and len(array) <= 3:
        return None
    elif array[1] == array[2] and len(array) <= 3:
        return None

    elif array[0] > array[1] > array[2]:
        max_0, max_1, max_2 = array[0], array[1], array[2]
    elif array[1] > array[2] > array[0]:
        max_0, max_1, max_2 = array[1], array[2], array[3]
    elif array[2] > array[0] > array[1]:
        max_0, max_1, max_2 = array[2], array[0], array[1]
    elif array[0] > array[2] > array[1]:
        max_0, max_1, max_2 = array[0], array[2], array[1]
    elif array[2] > array[1] > array[0]:
        max_0, max_1, max_2 = array[2], array[1], array[0]
    elif array[1] > array[0] > array[2]:
        max_0, max_1, max_2 = array[1], array[0], array[2]
    else:
        max_0, max_1, max_2 = array[0], array[1], array[2]

    for num in array[:]:
        if num > max_0:
            max_2 = max_1
            max_1 = max_0
            max_0 = num
        elif max_0 > num > max_1:
            max_2 = max_1
            max_1 = num
        elif max_1 > num > max_2:
            max_2 = num
    index = 2
    while (max_0 == max_1 or max_1 == max_2) and index < len(array):
        if max_0 > array[index]:
            max_1 = max_2
            max_2 = array[index]
        elif max_0 < array[index]:
            max_2 = max_1
            max_1 = max_0
            max_0 = array[index]

        elif max_1 > array[index]:
            max_2 = array[index]
        elif max_1 < array[index]:
            max_2 = max_1
            max_1 = array[index]
        index += 1

    if max_1 == max_2:
        return None
    return max_2


def test_thrid_max():
    result = thrid_max([])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([1])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([2, 2])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([2, 2, 2])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([1, 2, 3])
    assert result == 1, f'Wrong answer: {result}'
    result = thrid_max([2, 3, 1])
    assert result == 1, f'Wrong answer: {result}'
    result = thrid_max([2, 1, 3])
    assert result == 1, f'Wrong answer: {result}'
    result = thrid_max([1, 1, 2])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([11, 11, 22, 11, 11])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([11, 11, 10, 10, 10])
    assert result == None, f'Wrong answer: {result}'
    result = thrid_max([11, 22, 33, 44, 55])
    assert result == 33, f'Wrong answer: {result}'
    result = thrid_max([11, 11, 22, 33, 33, 44])
    assert result == 22, f'Wrong answer: {result}'
    result = thrid_max([11, 22, 22, 33, 33, 44])
    assert result == 22, f'Wrong answer: {result}'
    result = thrid_max([44, 44, 33, 33, 22, 33])
    assert result == 22, f'Wrong answer: {result}'
    result = thrid_max([44, 44, 44, 33, 33, 22, 33])
    assert result == 22, f'Wrong answer: {result}'
    result = thrid_max([1, 1, 2, 4, 2, 9, 23, 68])
    assert result == 9, f'Wrong answer: {result}'

    print('Третий максимум:', result)


if __name__ == '__main__':
    test_thrid_max()
