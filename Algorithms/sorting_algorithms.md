Алгоритмов сортировки:

```python
lst = [3, 2, 1, 4, 5]
sorted_lst = sorted(lst)
print(sorted_lst)

```

1. Сортировка выбором (Selection sort) - O(n^2)
    ```python
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    ```
2. Сортировка пузырьком (Bubble sort) - O(n^2)
    ```python
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    ```
3. Сортировка вставками (Insertion sort) - O(n^2)
    ```python
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    
    ```
4. Сортировка расческой (Comb sort) - O(n^2)
    ```python
    def comb_sort(arr):
        n = len(arr)
        gap = n
        shrink = 1.3
        swapped = True
        while gap > 1 or swapped:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(0, n-gap):
                j = i + gap
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    swapped = True
        return arr
    
    ```
5. Сортировка слиянием (Merge sort) - O(n log n)
    ```python
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    
    ```
6. Быстрая сортировка (Quick sort) - O(n log n)
    ```python
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    ```
7. Сортировка кучей (Heap sort) - O(n log n)
    ```python
    def heap_sort(arr):
        def sift_down(parent, limit):
            while 2*parent + 1 < limit:
                child = 2*parent + 1
                if child + 1 < limit and arr[child] < arr[child+1]:
                    child += 1
                if arr[parent] >= arr[child]:
                    break
    
    ```