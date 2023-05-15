def first_max(array):
    if len(array) < 1:
        return None
    max = array[0]
    for num in array[:]:
        if num > max:
            max = num
    return max


def test_first_max():
    result = first_max([])
    assert result == None, f'Wrong answer: {result}'
    result = first_max([8])
    assert result == 8, f'Wrong answer: {result}'
    result = first_max([4, 8, 88, -55])
    assert result == 88, f'Wrong answer: {result}'

    print('Первый максимум: ', result)


if __name__ == '__main__':
    test_first_max()
