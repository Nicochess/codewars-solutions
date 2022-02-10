def abbrev_name(name):
    index = 0
    for letter in name:
        index += 1
        if(letter == " "):
            return "{}.{}".format(name[0].upper(), name[index].upper())