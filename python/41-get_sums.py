def get_sum(a,b):
    return sum(list(range(b, a + 1))) if a > b else sum(list(range(a, b + 1)))