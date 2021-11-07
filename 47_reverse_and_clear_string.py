def reverse_letter(string):
    return "".join(l for l in string if l.isalpha())[::-1]