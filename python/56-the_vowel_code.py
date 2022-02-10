def encode(st):
    enc = str.maketrans("aeiou", "12345")
    return st.translate(enc)
    
def decode(st):
    enc = str.maketrans("12345", "aeiou")
    return st.translate(enc)