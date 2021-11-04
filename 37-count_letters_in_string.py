def count(string):
    occr = {}
    for letter in string:
        occr[letter] = string.count(letter)
    return occr