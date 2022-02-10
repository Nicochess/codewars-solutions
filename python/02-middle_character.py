def get_middle(s):
    index = int(len(s) / 2)
    return s[index - 1] + s[index] if len(s) % 2 == 0 else s[index]