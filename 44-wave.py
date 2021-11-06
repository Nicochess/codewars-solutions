def wave(people):
    list_people = []
    for index, letter in enumerate(people):
        if letter != " ":
            upper = people[index].upper()
            word = people[:index] + upper + people[index + 1:]
            list_people.append(word)
    return list_people