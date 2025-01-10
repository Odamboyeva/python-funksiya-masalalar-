def uzun_soz(list):
    list = []
    for i in list:
        a = max (list, key = len)
        return f"{a}, {len(a)}"
print(uzun_soz(['salom', 'ali', 'xiva', 'sdadsadsa']))