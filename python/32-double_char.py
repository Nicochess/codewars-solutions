def double_char(s):
    new_word = str()
    for letter in s:
        new_word += letter + letter
    return new_word