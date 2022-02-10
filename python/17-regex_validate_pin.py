import re
def validate_pin(pin):
    pattern = re.compile("^[0-9]{4}([0-9]{2})?")
    find = pattern.fullmatch(pin)
    return True if find else False