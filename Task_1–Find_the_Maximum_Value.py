def find_max(arr):
    max_number = arr[0]

    for value in arr:
        if value > max_number:
            max_number = value
    return max_number

print(find_max([-12, -9, -33, -20, -67]))