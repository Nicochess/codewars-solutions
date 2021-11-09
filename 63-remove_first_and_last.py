def array(string):
    str = " ".join(i for i in string.split(",")[1:-1])
    return str if str != "" else None