def two_min(array):
    if len(array) < 2:
        return None
    if array[0] < array[1]:
        max_1, max_2 = array[0], array[1]
    else:
        max_1, max_2 = array[1], array[0]

    index = 2
    while max_1 == max_2 and index < len(array):
        if max_1 > array[index]:
            max_1 = array[index]
        elif max_1 < array[index]:
            max_2 = array[index]
        index += 1

    if max_1 == max_2:
        return None

    for num in array[index:]:
        if num < max_1:
            max_2 = max_1
            max_1 = num
        elif num < max_2:
            max_2 = num

    return max_2


def test_two_min():
    result = two_min([1])
    assert result == None, f'Wrong answer: {result}'
    result = two_min([])
    assert result == None, f'Wrong answer: {result}'
    result = two_min([1, 3])
    assert result == 3, f'Wrong answer: {result}'
    result = two_min([1, 1, 1, 3])
    assert result == 3, f'Wrong answer: {result}'
    result = two_min([1, 5, 3, 8, 10])
    assert result == 3, f'Wrong answer: {result}'
    result = two_min([1, 5, 3, 8, 10, -1, -2])
    assert result == -1, f'Wrong answer: {result}'

    print('Второй минимум найден: ', result)


if __name__ == '__main__':
    test_two_min()
