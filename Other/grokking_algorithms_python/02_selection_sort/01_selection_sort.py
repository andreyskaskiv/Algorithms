# Finds the smallest value in an array
# Находит наименьшее значение в массиве
def findSmallest(arr):
    # Stores the smallest value
    smallest = arr[0]  # Для хранения наименьшего значения
    # Stores the index of the smallest value
    smallest_index = 0  # Для хранения индекса наименьшего элемента
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


# Sort array
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        # Находим наименьший элемент в массиве и добавляем его в новый массив
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# print(selectionSort([5, 3, 6, 2, 10]))

if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))
