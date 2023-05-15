def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


if __name__ == '__main__':
    print(find_max([55, 44, 66, 33, 77, 22, 88, 11]))
