def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            low = mid - 1
    return -1 
    
numbers = [4, 5, 8, 9, 11, 15, 100]
print(binary_search(numbers, 15))