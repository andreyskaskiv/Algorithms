def first_min(array):
    if len(array) < 1:
        return None
    min = array[0]
    for num in array[1:]:
        if num < min:
            min = num
    return min


def test_first_min():
    result = first_min([])
    assert result == None, f'Wrong answer: {result}'
    result = first_min([1])
    assert result == 1, f'Wrong answer: {result}'
    result = first_min([1, 4, 56, 2, -33, 5, 0])
    assert result == -33, f'Wrong answer: {result}'
    print(f'Все тесты пройдены: {result}')


if __name__ == '__main__':
    test_first_min()
