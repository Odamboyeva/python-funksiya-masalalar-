def ism_uzunligi(*ismlar):
    dict1 = {}
    for i in ismlar:
        dict1.update( { i : len(i) } )
    return dict1
print(ism_uzunligi("ali", "vali", "malik"))

