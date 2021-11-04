def filter_string(string):
    numbers = ""
    for elm in string:
        if elm in "0123456789":
            numbers += elm
    return int(numbers)