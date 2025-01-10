def kichkina(son, royhat):
    lst = []
    for i in royhat:
        if son < i:
            lst.append(i)
    return min (lst)

print(kichkina(5,[1,2,5,6,9,10]))