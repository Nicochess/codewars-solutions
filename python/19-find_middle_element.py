def gimme(input_array):
    middle_index = len(input_array) // 2
    sorted_array = sorted(input_array)
    return input_array.index(sorted_array[middle_index])