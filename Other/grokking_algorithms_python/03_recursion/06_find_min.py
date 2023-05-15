def find_min(arr):
    if len(arr) < 2:
        return None
    if len(arr) == 2 and arr[0] == arr[1]:
        return None
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    sub_min = find_min(arr[1:])
    return arr[0] if arr[0] < sub_min else sub_min


def test_find_min():
    result = find_min([])
    assert result == None, f'Wrong answer {result}'
    result = find_min([11, 11])
    assert result == None, f'Wrong answer {result}'
    result = find_min([11, 22])
    assert result == 11, f'Wrong answer {result}'
    # result = find_min([55, 55, 55])
    # assert result == 55, f'Wrong answer {result}'
    result = find_min([55, 44, 66, 33, 77, 22, 88, 11])
    assert result == 11, f'Wrong answer {result}'

    print('Задание выполнено !!!')


if __name__ == '__main__':
    test_find_min()
