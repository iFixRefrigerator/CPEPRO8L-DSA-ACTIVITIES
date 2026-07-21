def insert_at(values, index, new_value):
    if index < 0 or index > len(values):
        raise IndexError("Index out of range")
    
    values.append(None)

    for i in range(len(values) - 1, index, - 1):
        values[i] = values [i - 1]

    values[index] = new_value

    return values

print(insert_at([5, 10, 25, 70, 190], 2, 15))