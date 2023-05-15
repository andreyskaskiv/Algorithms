def two_max(array):
    if len(array) < 2:
        return None
    if array[0] == array[1] and len(array) <= 2:
        return None
    if array[0] > array[1]:
        max_1, max_2 = array[0], array[1]
    else:
        max_1, max_2 = array[1], array[0]

    for num in array[:]:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        if max_1 > num > max_2:
            max_2 = num

    index = 1
    while max_1 == max_2 and index < len(array):
        if max_1 > array[index]:
            max_2 = array[index]
        elif max_1 < array[index]:
            max_1 = array[index]
        index += 1
    if max_1 == max_2:
        return None
    return max_2


def test_two_max():
    result = two_max([])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([1])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([1, 1])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([22, 22, 22])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([11, 11, 22])
    assert result == 11, f'Wrong answer: {result}'
    result = two_max([22, 22, 11])
    assert result == 11, f'Wrong answer: {result}'
    result = two_max([11, 22, 22])
    assert result == 11, f'Wrong answer: {result}'
    result = two_max([11, 22, -11, 33, -44, 55])
    assert result == 33, f'Wrong answer: {result}'

    print('Все тесты пройдены')


if __name__ == '__main__':
    test_two_max()
