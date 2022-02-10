def nb_dig(n, d):
    nums = [str(num ** 2) for num in range(0, n + 1)]
    st = "".join(num for num in nums)
    return st.count(str(d))