def check_exam(arr1,arr2):
    total = 0
    for index, ans in enumerate(arr1):
        if arr1[index] == arr2[index]:
            total += 4
        elif arr2[index] == "":
            total += 0
        else:
            total -= 1
            
    return total if total >=0 else 0