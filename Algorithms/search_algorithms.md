1. Линейный поиск (Linear search) - O(n)
    ```python
    def linear_search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
    
    ```
2. Бинарный поиск (Binary search) - O(log n)
    ```python
    def binary_search(arr, x):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
    
    ```
3. Интерполяционный поиск (Interpolation search) - O(log log n) в лучшем случае, O(n) в худшем случае
   ```python
   def interpolation_search(arr, x):
       low = 0
       high = len(arr) - 1
       while low <= high and arr[low] <= x <= arr[high]:
           pos = low + (x - arr[low]) * (high - low) // (arr[high] - arr[low])
           if arr[pos] == x:
               return pos
           elif arr[pos] < x:
               low = pos + 1
           else:
               high = pos - 1
       return -1
   
   ```
4. Двоичный поиск по сегментам (Segmented binary search) - O(sqrt(n) * log n)
   ```python
   def segmented_binary_search(arr, x):
       n = len(arr)
       block_size = int(n ** 0.5)
       blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
       block_starts = [i*block_size for i in range(len(blocks))]
       block_ends = [(i+1)*block_size-1 for i in range(len(blocks)-1)] + [n-1]
   
       block_index = binary_search(block_starts, x)
       if block_index == -1:
           return -1
   
       start = block_starts[block_index]
       end = block_ends[block_index]
   
       index = binary_search(arr[start:end+1], x)
       if index == -1:
           return -1
   
       return start + index
   
   ```