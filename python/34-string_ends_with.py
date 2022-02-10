def solution(string, ending):
    index_start = len(string) - len(ending)
    return True if string[index_start:] == ending or ending == '' else False