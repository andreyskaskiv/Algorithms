#                             11  <   22  <  33  <  44
#                           min_1 < min_2 < min_3
def third_min(array):
    if len(array) < 3:
        return None
    if array[0] == array[1] == array[2] and len(array) <= 3:
        return None
    if array[0] == array[1] and len(array) <= 3:
        return None
    if array[1] == array[2] and len(array) <= 3:
        return None
    elif array[0] < array[1] < array[2]:
        min_1, min_2, min_3 = array[0], array[1], array[2]
    elif array[1] < array[2] < array[0]:
        min_1, min_2, min_3 = array[1], array[2], array[3]
    elif array[2] < array[0] < array[1]:
        min_1, min_2, min_3 = array[2], array[0], array[1]
    elif array[0] < array[2] < array[1]:
        min_1, min_2, min_3 = array[0], array[2], array[1]
    elif array[2] < array[1] < array[0]:
        min_1, min_2, min_3 = array[2], array[1], array[0]
    elif array[1] < array[0] < array[2]:
        min_1, min_2, min_3 = array[1], array[0], array[2]
    else:
        min_1, min_2, min_3 = array[0], array[1], array[2]

    for num in array[:]:
        if num < min_1:
            min_3 = min_2
            min_2 = min_1
            min_1 = num
        elif min_1 < num < min_2:
            min_3 = min_2
            min_2 = num
        elif min_2 < num < min_3:
            min_3 = num

    index = 1

    while (min_1 == min_2 or min_2 == min_3) and index < len(array):
        if min_1 < array[index]:
            min_2 = min_3
            min_3 = array[index]
        elif min_1 > array[index]:
            min_3 = min_2
            min_2 = min_1
            min_1 = array[index]

        elif min_2 < array[index]:
            min_3 = array[index]
        elif min_2 > array[index]:
            min_3 = min_1
            min_2 = array[index]
        index += 1

    if min_2 == min_3 or min_1 == min_2:
        return None
    return min_3


def test_third_min():
    result = third_min([])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([1])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([2, 2])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([2, 2, 2])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([1, 2, 3])
    assert result == 3, f'Wrong answer: {result}'
    result = third_min([2, 3, 1])
    assert result == 3, f'Wrong answer: {result}'
    result = third_min([2, 1, 3])
    assert result == 3, f'Wrong answer: {result}'
    result = third_min([1, 1, 2])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([11, 11, 22, 11, 11])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([11, 11, 10, 10, 10])
    assert result == None, f'Wrong answer: {result}'
    result = third_min([11, 22, 33, 44, 55])
    assert result == 33, f'Wrong answer: {result}'
    result = third_min([11, 11, 22, 33, 33, 44])
    assert result == 33, f'Wrong answer: {result}'
    result = third_min([11, 22, 22, 33, 33, 44])
    assert result == 33, f'Wrong answer: {result}'
    result = third_min([44, 44, 33, 33, 22, 33])
    assert result == 44, f'Wrong answer: {result}'
    result = third_min([44, 44, 44, 33, 33, 22, 33])
    assert result == 44, f'Wrong answer: {result}'
    result = third_min([1, 1, 2, 4, 2, 9, 23, 68])
    assert result == 4, f'Wrong answer: {result}'

    print('Все тесты пройдены')


if __name__ == '__main__':
    test_third_min()
