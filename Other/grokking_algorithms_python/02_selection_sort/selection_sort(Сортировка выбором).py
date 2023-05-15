# 1. Находим наименьшее значение в массиве и его индекс,
# потом возвращаем индекс минимального элемента
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# Теперь на основе ф-и findSmallest отсортируем массив
def selectionSort(arr):
    newArr = []  # В пустой массив будем добавлять элементы по возрастанию
    for i in range(len(arr)):  # Находим наименьший элемент в массиве и добавляем его в новый массив
        smollest = findSmallest(arr)
        newArr.append(arr.pop(smollest))  # аппендим в новый массив элемент за наименьшим индексом
    return newArr


if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    print('Массив на входе      ', arr)
    print('Отсортированый массив', selectionSort(arr))
    print('O(n^2)')
